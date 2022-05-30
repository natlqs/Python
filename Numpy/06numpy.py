# numpy 索引

import numpy as np

a = np.arange(3, 15)        # 创建
print(a)
print(a[3])             # 第4个元素


a = a.reshape((3, 4))       # 重新排列为3行4列
print(a)
print(a[2])                 # 第3行
print(a[2][1])              # 第3行，第2列的元素
print(a[2, 1])


for row in a:
    print(row)          # 循环打印每一行

for column in a.T:      # 转置，行变列，列变行
    print(column)       # 循环打印每一行


for item in a.flat:         # 将矩阵转置成单行
    print(item)

print(a.flatten())      # 展平
print(a.flat)