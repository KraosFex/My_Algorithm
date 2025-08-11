## Script Python Gráfico Python en Power BI

# Importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Importing auto_arima
from pmdarima.arima import auto_arima

#Convert the month column to datetime
dataset['AñoMes']=pd.to_datetime(dataset['AñoMes'])

#Set the index of the Month
dataset.set_index('AñoMes',inplace=True)

#Testing for stationarity
from pmdarima.arima import ADFTest
adf_test = ADFTest(alpha = 0.05)
adf_test.should_diff(dataset)

#Spliting the dataset into train and test
train = dataset[:85]
test = dataset[-20:]

arima_model =  auto_arima(train,start_p=0, d=1, start_q=0,
                          max_p=5, max_d=5, max_q=5, start_P=0,
                          D=1, start_Q=0, max_P=5, max_D=5,
                          max_Q=5, m=12, seasonal=True,
                          error_action='warn',trace = True,
                          supress_warnings=True,stepwise = True,
                          random_state=20,n_fits = 50)


prediction = pd.DataFrame(arima_model.predict(n_periods = 20),index=test.index)
prediction.columns = ['predicted_sales']
prediction

plt.figure(figsize=(12,8))
plt.plot(train,label="Training")
plt.plot(test,label="Test")
plt.plot(prediction,label="Predicted")
plt.legend(loc = 'best')
plt.xticks(rotation=45)
plt.show()
