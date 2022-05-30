# 随机数组，最大值，最小值，
import numpy as np

a = np.random.random((2, 4))

print(a)
print(np.sum(a))
print(np.min(a))
print(np.max(a))

print(np.sum(a, axis=1))        #  axis = 1, 在行中求和
print(np.min(a, axis=0))        # axis = 0, 找列中的最小值
print(np.max(a, axis=1))        # 在行中的最大值