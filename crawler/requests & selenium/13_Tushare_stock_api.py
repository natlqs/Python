import tushare as ts
df = ts.get_hist_data('600519', start = '2018-01-01', end='2020-11-11')
print(df)