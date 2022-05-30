# numpy 和array的合并
import numpy as np
a = np.array([1, 2, 3])
b = np.array([2, 2, 2])

c = np.vstack((a, b))        # vertical 上下合并，变成2行3列的矩阵
print(c)

d = np.hstack((a, b))        # Horizontal 左右合并
print(d)

print(a.shape, c.shape)
print(d.shape)

e = a[:, np.newaxis]        # 将序列转换成纵向
print(e)
f = b[:, np.newaxis]        
print(f)

g = np.vstack((e, f))
print(g)
h = np.hstack((e, f))
print(h)