from operator import index
import PIL
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_excel('.\\Python\\crawler\\Pandas & Mysql\\股票型基金.xlsx')
data = data.drop(columns=['基金代码'])
data = data[['日增长率', '近1周', '近1月', '近3月', '近6月', '近1年', '近2年', '近3年', '今年来', '成立来']]
# plt.plot(str(data.iloc[1]), data.columns.values)
print(data.iloc[1].tolist())
print(data.iloc[2].tolist())

plt.plot(data.iloc[1].to_list(), marker='o')
plt.plot(data.iloc[2].to_list(), marker = 'o')
plt.plot(data.iloc[3].to_list(), marker = 'o')
plt.plot(data.iloc[4].to_list(), marker = 'o')
plt.plot(data.iloc[5].to_list(), marker = 'o')
plt.plot(data.iloc[6].to_list(), marker = 'o')
plt.plot(data.iloc[7].to_list(), marker = 'o')
plt.plot(data.iloc[9].to_list(), marker = 'o')
plt.show()
