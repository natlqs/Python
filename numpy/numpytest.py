
import numpy as np
a = [1, 2, 3, 4]
b = np.array(a)
print(b)
type(b)

print(b.shape)          # 返回 (列数， 行数)
print(b.argmax())      #argmax返回的是最大数的'索引'.argmax有一个参数axis,默认是0,表示每一列的最大值的索引 axis=1表示每一行的最大值的索引
print(b.max())        # max 返回的是最大的值
print(b.mean())        # 返回均值


c = [[1, 2], [3, 4]]        # 二维
d = np.array(c)
print(c)
print(d)             # 二维numpy数组
d.shape         # (2, 2)
d.size          # 4  size return the number of element of the array
d.max(axis=0)           # 找行的最大值， array([3, 4])
d.max(axis=1)           # 找列的最大值， array([2, 4])
d.mean(axis=0)          # 找行的均值， array（[2., 3.])
d.flatten()             # 展开一个numpy数组为1维数组， array（[1, 2, 3, 4])
np.ravel(c)             # 展开一个可以解析的结构为1维的数组， array([1, 2, 3, 4])

# 3x3的浮点型2维数组，并且初始化所有元素值为1
e = np.ones((3, 3), dtype=np.float)
print(3)

# 创建个一维数组，元素值是把3重复4次， array（[3, 3, 3, 3])
f = np.repeat(3, 4)
print(f)
