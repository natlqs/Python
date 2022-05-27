# 简单计算 + - * /
import numpy as np
a = np.array([[10, 20, 30, 40], [2, 3, 4, 5]])
b = np.arange(8).reshape((2, 4))
print(a, b)
print(b<3)
print(b == 3)

c = a - b
print(c)

d = a + b
print(d)

e = a * b           # 按位相乘即相对应元素之间的乘法   非矩阵乘法，矩阵乘法： np.dot(a, b)
print(e)

f = a / b
print(f)

g = a * 10
print(g)

h = 10 * np.sin(a)
print(h)


