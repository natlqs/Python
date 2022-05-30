# 导入numpy， 输出数组的形状， 几个元素， 几行
import numpy as np
array = np.array([[1, 2, 3], [2, 3, 4]])

print(array)
print('number of dimension:', array.ndim)       # 数组的维数    
print('shape:', array.shape)            # 数组的形状，几行几列
print('size:', array.size)      #   数组的元素个数
