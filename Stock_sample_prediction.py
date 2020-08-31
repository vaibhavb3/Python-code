# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 09:58:36 2019

@author: Lenovo
"""

import os
from statsmodels.tsa.api import SimpleExpSmoothing, Holt, ExponentialSmoothing
import pandas as pd
import os

os.getcwd()
os.chdir("C:\\Users\\Lenovo\\Documents\\Vaibhav\\python")
os.getcwd()

Fullraw = pd.read_csv("Bank_Nifty.csv", encoding = "ISO-8859-1")
Fullraw.isnull().sum()

Fullraw2 = Fullraw.groupby('Date')['Open'].sum().reset_index().copy()

Fullraw2['Date'] = pd.to_datetime(Fullraw2['Date'])
Fullraw2.set_index('Date', inplace =True)

Fullraw3 = Fullraw2['Open'].resample('1W').mean()

import seaborn as sns
sns.lineplot(data = Fullraw3)

from statsmodels.tsa.seasonal import seasonal_decompose
Decomposed_Series = seasonal_decompose(Fullraw3)
Decomposed_Series.plot()

Train = Fullraw3[:36]
Test = Fullraw3[36:]

SES = SimpleExpSmoothing(Train).fit(smoothing_level=0.01)
Forecast = SES.forecast(12).rename('Forecast')
Actual_Forecast_Df = pd.concat([Fullraw3, Forecast], axis =1)


sns.lineplot(data = Actual_Forecast_Df)

import numpy as np
Validation_Df = Actual_Forecast_Df[-12:].copy()
np.mean(abs(Validation_Df['Open'] -Validation_Df['Forecast'])/Validation_Df['Open'])*100  #MAPE################
np.sqrt(np.mean((Validation_Df['Open']- Validation_Df['Forecast'])**2)) ####RMSE######

Train.mean()

###########  DES   ###########
DES = Holt(Train).fit(smoothing_level=0.01, smoothing_slope=0.1)
Forecast_DS = SES.forecast(12).rename('Forecast')
Actual_Forecast_Df_DS = pd.concat([Fullraw3, Forecast_DS], axis =1)
sns.lineplot(data = Actual_Forecast_Df_DS)

Validation_Df_DS = Actual_Forecast_Df_DS[-12:].copy()
np.mean(abs(Validation_Df_DS['Open'] -Validation_Df_DS['Forecast'])/Validation_Df_DS['Open'])*100  #MAPE################
np.sqrt(np.mean((Validation_Df_DS['Open']- Validation_Df_DS['Forecast'])**2)) ####RMSE######


TES = ExponentialSmoothing(Train,
                           seasonal_periods = 12,
                           seasonal = 'add',
                           trend = 'add').fit(smoothing_level=0.01,
                                        smoothing_slope=0.1,
                                        smoothing_seasonal=0.3)
Forecast = TES.forecast(12).rename('Forecast')
Actual_Forecast_Df = pd.concat([Fullraw3, Forecast], axis =1)

sns.lineplot(data = Actual_Forecast_Df)

Validation_Df =Actual_Forecast_Df[-12:].copy()
np.mean(abs(Validation_Df['Open'] -Validation_Df['Forecast'])/Validation_Df['Open'])*100  #MAPE################
np.sqrt(np.mean((Validation_Df['Open']- Validation_Df['Forecast'])**2))


TES2 = ExponentialSmoothing(Train,
                           seasonal_periods = 12,
                           seasonal = 'add',
                           trend = 'add').fit()

                            
TES2.summary()

Forecast_2 = TES2.forecast(12).rename('Forecast_2')
Actual_Forecast_Df = pd.concat([Fullraw3, Forecast_2], axis =1)

sns.lineplot(data = Actual_Forecast_Df)

Validation_Df =Actual_Forecast_Df[-12:].copy()
np.mean(abs(Validation_Df['Sales'] -Validation_Df['Forecast_2'])/Validation_Df['Open'])*100  #MAPE################
np.sqrt(np.mean((Validation_Df['Open']- Validation_Df['Forecast_2'])**2))
