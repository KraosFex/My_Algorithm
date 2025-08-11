# Script Python para Clustering Kmeans

# Carga de librerias
import pyodbc
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.spatial import distance as sci_distance
from sklearn import cluster as sk_cluster

# Database connection
conn_str = pyodbc.connect(
    '''DRIVER={ODBC Driver 17 for SQL Server}; 
       SERVER=<server>; 
       DATABASE=tpcxbb_1gb; 
       UID=<username>; 
       PWD=<password>'''
       )

# SQL Query for the preparation of the data that will later be analyzed by the algorithm
input_query = '''SELECT ss_customer_sk AS customer,
                 ROUND(COALESCE(returns_count / NULLIF(1.0*orders_count, 0), 0), 7) AS orderRatio,
                 ROUND(COALESCE(returns_items / NULLIF(1.0*orders_items, 0), 0), 7) AS itemsRatio,
                 ROUND(COALESCE(returns_money / NULLIF(1.0*orders_money, 0), 0), 7) AS monetaryRatio,
                 COALESCE(returns_count, 0) AS frequency
                 FROM
                 ( 
                 SELECT ss_customer_sk, 
                 -- return order ratio COUNT(distinct(ss_ticket_number)) AS orders_count,
                 -- return ss_item_sk ratio COUNT(ss_item_sk) AS orders_items,
                 -- return monetary amount ratio SUM( ss_net_paid ) AS orders_money
                 FROM store_sales s GROUP BY ss_customer_sk 
                 ) 
                 orders LEFT OUTER JOIN 
                 ( 
                 SELECT sr_customer_sk,
                 -- return order ratio count(distinct(sr_ticket_number)) as returns_count,
                 -- return ss_item_sk ratio COUNT(sr_item_sk) as returns_items,
                 -- return monetary amount ratio SUM( sr_return_amt ) AS returns_money
                 FROM store_returns GROUP BY sr_customer_sk 
                 ) 
                 returned ON ss_customer_sk=sr_customer_sk'''
##################

# Guardamos en un avariable el resultado del procedimiento read_sql de pd(libreria pandas)
## Este procedimiento recibe la conexion a la base de datos y Query
customer_data = pd.read_sql(input_query, conn_str)

#######################

# Con esta linea se puede imprimir los primeros datos almacenados en la variable previamente creada
## note que en --> customer_data.head(n=5) // la n es la varible que define cuantas filas de datos se imprimiran, pruba primero imprimir 5 y luego 7
#print("Data frame:", customer_data.head(n=5))

##########################

## numero de clusters usando el Elbow method, Este paso es necesario para posteriormente analizar los datos y el clusterizado 
cdata = customer_data
K = range(1, 20)
KM = (sk_cluster.KMeans(n_clusters=k).fit(cdata) for k in K)
centroids = (k.cluster_centers_ for k in KM)

D_k = (sci_distance.cdist(cdata, cent, 'euclidean') for cent in centroids)
dist = (np.min(D, axis=1) for D in D_k)
avgWithinSS = [sum(d) / cdata.shape[0] for d in dist]
plt.plot(K, avgWithinSS, 'b*-')
plt.grid(True)
plt.xlabel('Number of clusters')
plt.ylabel('Average within-cluster sum of squares')
plt.title('Elbow for KMeans clustering')
plt.show()

## clustering usando Kmeans, se agrupan los datos en clusteres y luego se devuelve la metrica
n_clusters = 4

means_cluster = sk_cluster.KMeans(n_clusters=n_clusters, random_state=111)
columns = ["orderRatio", "itemsRatio", "monetaryRatio", "frequency"]
est = means_cluster.fit(customer_data[columns])
clusters = est.labels_
customer_data['cluster'] = clusters

# For each cluster, count the members. 
for c in range(n_clusters):
    cluster_members=customer_data[customer_data['cluster'] == c][:]
    print('Cluster{}(n={}):'.format(c, len(cluster_members)))
    print('-'* 17)
    print(customer_data.groupby(['cluster']).mean())

#centroides = means_cluster.cluster_centers_
#print(centroides)

#customer_data.columns
#print(customer_data)



