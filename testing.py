# -*- coding: utf-8 -*-
"""
Created on Fri May 01 19:17:47 2015

@author: NWB066
"""

import pandas as pd
import pandas.io.data as web
import datetime
import dateutil.relativedelta
import matplotlib.pyplot as plt
import numpy as np
import scipy
import scipy.interpolate
import sklearn.ensemble


asset = 'SCHA'    #Define list of assets to evaluate
PredictionHorizon = 7              #PredictionHorizon in calendar days
threshold = 0.01
#start_dt =datetime.datetime.now() - dateutil.relativedelta.relativedelta(years=7)     # start date of price history
start_dt = datetime.datetime(2007,1,1)  # start date of price history
end_dt = datetime.datetime.now()      # end date of price history




Prices = pd.DataFrame(index=pd.date_range(start=start_dt,end=end_dt,freq='h'))
Prices.sort_index(inplace=True)
Prices['dummy']=1
    
temp = web.DataReader(asset,'yahoo',start=start_dt,end=end_dt)                 #Pull asset's data from Yahoo
temp_opens = pd.DataFrame(temp['Open'])                                        #Parse open and close prices
temp_opens['Price'] = temp_opens['Open']
del temp_opens['Open']
temp_opens.index = temp_opens.index + pd.DateOffset(hours=9.5)
temp_closes = pd.DataFrame(temp['Close'])
temp_closes['Price'] = temp_closes['Close']
del temp_closes['Close']
temp_closes.index = temp_closes.index + pd.DateOffset(hours=16)
temp_final = pd.concat([temp_opens,temp_closes])                               #Combine open and close data
temp_final.sort_index(inplace=True)
Prices = Prices.merge(temp_final,how='outer',left_index=True,right_index=True) #Join to Prices table
Prices.sort_index(inplace=True)
Prices['Price'] = Prices['Price'].interpolate(method='linear')                #Interpolate missing values
##Prices['Price'].interpolate(method='spline',order=3,inplace=True)                #Interpolate missing values
Prices.dropna(axis=0,inplace=True)                                             #Drop any records with NULLs
    
print Prices.head(3)
