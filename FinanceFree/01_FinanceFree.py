import yfinance as yf
import datetime as dt
import pandas as pd

from pandas_datareader import data as pdr

yf.pdr_override()
start = dt.datetime(1980, 12, 1)
now = dt.datetime.now()
stock = ""
stock = input('enter the stock symbol:   ')
df = pdr.get_data_yahoo(stock, start, now)
print(df)
lastGLV = []

def GLV():
    dfmonth = df.groupby(pd.Grouper(freq='M'))['High'].max()
    # print(dfmonth)

    glDate = 0
    currentDate = ""
    currentGlV = 0

    for index, value in dfmonth.items():
        if value > currentGlV:
            currentGlV = value
            currentDate = index
            counter=0
        if value < currentGlV:
            counter = counter + 1
        
            if counter==3 and ((index.month != now.month) or (index.year != now.year)):
                if currentGlV != lastGLV:
                    print(currentGlV)
                glDate=currentDate
                # lastGLV=currentGlV
                lastGLV.append(currentGlV)

        # print(str(lastGLV))
    print('压力值:', lastGLV)

#  交易策略/买入卖出时机
# percentchange = []
def BuySell():
    percentchange = []
    numBuy = 0
    numSell = 0
    num = 0
    pos = 0
    bp = 0
    sp = 0
    # for j in lastGLV:
    for i in df.index:
        num = 0
        close = df['Adj Close'][i]
        if (close > lastGLV[num] and pos == 0):
            bp = close
            pos = 1
            numBuy +=1
            print('buying now at ' + str(bp) + str(i))
        if close > 1.25*bp and pos == 1:
            pos = 0
            sp = close
            numSell +=1
            pc = (sp/bp-1)*100         # profit 
            percentchange.append(pc)
            print('selling now at ' + str(sp) + str(i))
            if sp > lastGLV[num]:
                num += 1
                print("this Green Line doesn't make sense anymore")
        elif close < 0.85*bp and pos ==1:
            pos = 0
            sp = close
            numSell +=1
            pc = (sp/bp-1)*100         # profit 
            percentchange.append(pc)
            print('selling now for safety' + str(sp) + str(i))
            if sp > lastGLV[num]:
                num += 1
                print("this Green Line doesn't make sense anymore")
        else:
            pass
    gains = 0
    ng = 0      # number of gains
    losses = 0
    nl = 0      # number of losses
    totalr = 1  # total of returns / revenue
    print(numBuy, numSell)


    # calculate porflio percentchange
    for i in percentchange:
        if(i>0):
            gains += i
            ng += 1
        else:
            losses +=i
            nl +=1
        totalr = totalr*((i/100) +1)

    totalr = round((totalr-1)*100, 2)
    print(totalr)


GLV()
BuySell()



'''
    for i in df.index:
        close = df['close'][i]
        if(close > lastGLV[0] ):
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
'''