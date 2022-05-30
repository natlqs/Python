import tushare as ts
stock = input('please input the stock number:')
df = ts.get_hist_data(stock, start = '2021-07-01', end='2022-05-11')
print(df)