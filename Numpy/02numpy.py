# 创建各种numpy数组

import numpy as np
a = np.array([[2, 23, 4],       # 创建
              [2, 3, 4]])
print(a)

b = np.zeros([3, 4])            # 都是0
print(b)


c = np.ones((3, 4), dtype= int)     # 都是1， 可以指定数据类型
print(c)

d = np.empty((3, 4))            # 空，其实是0
print(d)

e = np.arange(10, 20, 2)        # 创建单行数组，间隔为2， 从10开始到20结束
print(e)


f = np.arange(12).reshape((3, 4))       # 转换为3行3列
print(f)


g = np.linspace(1, 10, 5)           # 把从1 到 10 平均分为5 段
print(g)


h = np.linspace(1, 20, 6).reshape((2, 3))       # 1 到20平均分为6段，并将结果转换为2*3 的数组
print(h)

