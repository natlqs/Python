import pandas as pd
import numpy as np
# import yfinance as yf
import tushare as ts
import datetime as dt
from pandas_datareader import data as pdr
# yf.pdr_override()

stock = input("Enter a stock ticker symbol: ")
# print(stock)
startyear = 2011
startmonth = 7
startday = 1

start= dt.datetime(startyear, startmonth, startday)
now = dt.datetime.now()

df = ts.get_hist_data(stock, start = str(start), end = str(now))
print(df)
ma = 50
smaString = 'sma' + str(ma)

df[smaString] = df.iloc[:,3].rolling(window=ma).mean()
df = df.iloc[ma:]
emasUsed = [3, 5, 8, 10, 12, 15, 30, 35, 40, 45, 50, 60]
for x in emasUsed:
    ema = x
    df['ema_' + str(x)] = round(df.iloc[:, 3].ewm(span=ema, adjust=False).mean(), 2)
# print(df.tail())
pos = 0
num = 0
percentchange = []

for i in df.index:
    cmin = min(df['ema_3'][i], df['ema_5'][i],  df['ema_8'][i], df['ema_10'][i], df['ema_12'][i], df['ema_15'][i],)
    cmax = max(df['ema_30'][i], df['ema_35'][i],  df['ema_40'][i], df['ema_45'][i], df['ema_50'][i], df['ema_60'][i],)
    close = df['close'][i]
    if(cmin > cmax):
        print('red white blue')
        if (pos ==0):
            bp = close          # bp: buy price
            pos = 1
            print('buying now at ' + str(bp))
        
    elif(cmin < cmax):
        print('blue white blue')
        if (pos == 1):
            pos = 0
            sp = close          # sp: sell price 
            print('selling now at ' + str(sp))
            pc = (sp/bp-1)*100         # profit 
            percentchange.append(pc)

    if (num == df['close'].count() -1 and pos ==1):
        pos = 0
        sp = close
        print('selling now at ' + str(sp))
        pc = (sp/bp-1) * 100
        percentchange.append(pc)
    num +=1
print(percentchange)

gains = 0
ng = 0      # number of gains
losses = 0
nl = 0      # number of losses
totalr = 1  # total of returns / revenue

for i in percentchange:
    if(i>0):
        gains += i
        ng += 1
    else:
        losses +=i
        nl +=1
    totalr = totalr*((i/100) +1)

totalr = round((totalr-1)*100, 2)


if (ng>0):
    avggain = gains/ng
    maxr = str(max(percentchange))
else:
    avggain = 0
    maxr = 'undifined'

if (nl>0):
    avgloss = losses/nl
    maxl = str(min(percentchange))
    ratio = str(-avggain/avgloss)       # gain/loss ratio
else:
    avgloss = 0
    maxl = 'undifined'
    ratio = 'inf'

if(ng>0 or nl > 0):
    battingavg = ng/(ng+nl)     # win rate
else:
    battingavg=0

print()
print("Results for "+ stock +" going back to "+str(df.index[0])+", Sample size: "+str(ng+nl)+" trades")
print("EMAs used: "+str(emasUsed))
print("Batting Avg: "+ str(battingavg))
print("Gain/loss ratio: "+ ratio)
print("Average Gain: "+ str(avggain))
print("Average Loss: "+ str(avgloss))
print("Max Return: "+ maxr)
print("Max Loss: "+ maxl)
print("Total return over "+str(ng+nl)+ " trades: "+ str(totalr)+"%" )
#print("Example return Simulating "+str(n)+ " trades: "+ str(nReturn)+"%" )
print()
