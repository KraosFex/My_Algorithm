# Script Python Análisis de sentimiento

# Cargar paquetes
import pyodbc
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import nltk

# Conexion a la base de datos
conn_str = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER=LENOVO\SQLEXPRESS; DATABASE=tpcxbb_1gb; UID=<username>; PWD=<password>')

# Query SQL para la preparacion de los datos que luego seran analizados por el algorit de analicis de sentimientos
input_query = '''SELECT 
                    T0.pr_review_date AS FechaReview,
                    T0.pr_item_sk AS ProductID,
                    T0.pr_review_rating AS Calificacion,
                    T0.pr_review_content AS Review,
                    T0.pr_user_sk AS Usuario,
                    T1.i_category AS Categoria,
                    T1.i_product_name AS Producto,
                    T1.i_item_desc AS Descripcion,
                    T1.i_size AS tamaño
                 FROM product_reviews T0
                 join item T1 ON T0.pr_item_sk = T1.i_item_sk'''

###################################################

reviews_data = pd.read_sql(input_query, conn_str)


###################################################


print("Data frame:", reviews_data.head(n=5))


##################################################

from nltk.sentiment.vader import SentimentIntensityAnalyzer

sent = SentimentIntensityAnalyzer()

df = pd.DataFrame(data=reviews_data)

polarity = [round(sent.polarity_scores(i)['compound'], 2) for i in df['Review']]
df['sentiment_score'] = polarity