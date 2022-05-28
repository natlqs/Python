# 简单计算2
import numpy as np
a = np.arange(2, 14).reshape((3, 4))



print(a)                    
print(np.mean(a))           # 平均值
print(a.mean())

print(np.argmin(a))        # 最小值的索引
print(a.argmin())

print(np.argmax(a))         # 最大值的索引
print(a.argmax())

print(np.median(a))         #  中位数

print(np.cumsum(a))         # 累加
print(a.cumsum())   

print(np.diff(a))           # 累差，每两个数的差


print(np.nonzero(a))        # 找出非0数的位置

print(np.sort(a))           # 排序

print(np.transpose(a))      # 行变成列，列变成行

print(np.clip(a, 3, 9))     # 截取矩阵， 小于3 的都变成3， 大于9的都变成9，其他的不变

