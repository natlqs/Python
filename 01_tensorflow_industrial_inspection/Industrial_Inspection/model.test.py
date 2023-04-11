import numpy as np
import keras
from keras.models import Sequential,load_model
from keras.layers import Dense, Dropout, Flatten,Input
from keras.layers import Conv2D, MaxPooling2D,merge
from keras.layers import BatchNormalization,Activation
from sklearn.model_selection import train_test_split
from keras.optimizers import SGD
from keras.models import Model
import tensorflow as tf
from PIL import Image,ImageDraw,ImageFont
from image_handle import *
import os
import cv2

from keras import backend as K
K.clear_session()

start=10
end=11
image_number=1451
resize_width=300
resize_height=300

image_resize=[]
image_vector=[]
image_label=[]
image_label_list=['擦花','漏底','碰凹','凸粉']  #漏底占的比例太大了，导致后面的预测全部都偏向该物体
data = np.empty((22,300, 300,3), dtype="float32")
image_dir='C:/Users/18301/Desktop/test_image/'

data,image_label,image_vec=get_image_data(image_dir,resize_width,resize_height,data,image_label,image_label_list)
#准备好数据和标签送进VGG网络中
X_train=data
Y_train = keras.utils.to_categorical(image_label,4) #转换成one-hot向量

# print(X_train)
print(Y_train)
x_train=X_train[start:end]
y_train=Y_train[start:end]

model = load_model('model_google_layer.h5')
preds = model.predict(x_train)

print(preds)
list_pre= preds[0].tolist()

object_index=list_pre.index(max(list_pre))


y_=Y_train[start:end][0]
y_=y_.tolist()
print(y_)

true_object_index=y_.index(max(y_))

print(object_index)
print(true_object_index)

s_pre=image_label_list[object_index]
s_true=image_label_list[true_object_index]

print(s_pre)
print(s_true)

image=image_vec[start]
draw = ImageDraw.Draw(image)
############注意：这里检测出来的物体种类，擦花由于特征不够明显，基本上被判断成凸粉，这一点需要改善#################
s_pre_out='检测出的缺陷种类为：'+s_pre
s_true_out='真实缺陷种类为：'+s_true

print(s_pre_out)
print(s_true_out)

ttfront = ImageFont.truetype('simhei.ttf', 20)#字体大小

draw.text((30,40),str(s_pre_out), fill = (255, 0 ,0), font=ttfront)
draw.text((50,60),str(s_true_out), fill = (255, 0 ,0), font=ttfront)

image.show()

from keras import backend as K
K.clear_session()
