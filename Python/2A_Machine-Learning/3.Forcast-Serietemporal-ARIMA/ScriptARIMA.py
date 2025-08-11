## Script Python ARIMA

# Importing necessary libraries
import pyodbc
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings('ignore')

# Importing auto_arima
from pmdarima.arima import auto_arima

# Database connection
conn_str = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER=<server>; DATABASE=tpcxbb_1gb; UID=<username>; PWD=<password>')

# SQL Query for the preparation of the data that will later be analyzed by the algorithm
input_query = '''SELECT
                 CONCAT_WS('-',YEAR(T1.d_date), MONTH(T1.d_date)) AS AñoMes,
                 SUM(T0.ss_quantity * T0.ss_list_price) AS Ventas
                 FROM store_sales T0
                    join date_dim T1 ON T0.ss_sold_date_sk = T1.d_date_sk
                 WHERE CONCAT_WS('-',YEAR(T1.d_date), MONTH(T1.d_date)) <> '2005-12'
                 GROUP BY YEAR(T1.d_date), MONTH(T1.d_date)
                 ORDER BY YEAR(T1.d_date), MONTH(T1.d_date)'''

##################

sales_data = pd.read_sql(input_query, conn_str)

sales_data.head()

#Make sure there are no null values at the end of the dataset
sales_data.tail()

#Check the datatypes
sales_data.dtypes

#Convert the month column to datetime
sales_data['AñoMes']=pd.to_datetime(sales_data['AñoMes'])


#Recheck the datatypes
sales_data.dtypes

#Set the index of the Month
sales_data.set_index('AñoMes',inplace=True)

sales_data.head()

# To understand the pattern
sales_data.plot()


#Testing for stationarity
from pmdarima.arima import ADFTest
adf_test = ADFTest(alpha = 0.05)
adf_test.should_diff(sales_data)

#Spliting the dataset into train and test
train = sales_data[:85]
test = sales_data[-20:]

train.tail()

test.head()

plt.plot(train)
plt.plot(test)

arima_model =  auto_arima(train,start_p=0, d=1, start_q=0,
                          max_p=5, max_d=5, max_q=5, start_P=0,
                          D=1, start_Q=0, max_P=5, max_D=5,
                          max_Q=5, m=12, seasonal=True,
                          error_action='warn',trace = True,
                          supress_warnings=True,stepwise = True,
                          random_state=20,n_fits = 50 )

#Summary of the model
arima_model.summary()

prediction = pd.DataFrame(arima_model.predict(n_periods = 20),index=test.index)
prediction.columns = ['predicted_sales']
prediction

plt.figure(figsize=(8,5))
plt.plot(train,label="Training")
plt.plot(test,label="Test")
plt.plot(prediction,label="Predicted")
plt.legend(loc = 'best')
plt.show()

from sklearn.metrics import r2_score
test['predicted_sales'] = prediction
r2_score(test['Ventas'], test['predicted_sales'])

data_final = pd.concat([sales_data, prediction], axis=0)
