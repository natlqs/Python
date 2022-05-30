# get stock history price 
# store as file
# Draw the K picture
import matplotlib
from matplotlib.pyplot import ylabel
import pandas as pd
import numpy as np
# import yfinance as yf
import datetime as dt
import tushare as ts
# from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
import mplfinance as mpf


# yf.pdr_override()       # 

start = dt.datetime(1980, 12, 1)
now = dt.datetime.now()

stock=input('Input the stock symbol:   ')
df = ts.get_hist_data(stock, start= str(start), end = str(now))
# print(df)

df2 = df['close']
mpf.plot(df2, type='candle', title='Candlestick', ylabel='price(RMB)')