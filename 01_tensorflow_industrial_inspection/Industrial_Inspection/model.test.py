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
image_label_list=['����','©��','����','͹��']  #©��ռ�ı���̫���ˣ����º����Ԥ��ȫ����ƫ�������
data = np.empty((22,300, 300,3), dtype="float32")
image_dir='C:/Users/18301/Desktop/test_image/'

data,image_label,image_vec=get_image_data(image_dir,resize_width,resize_height,data,image_label,image_label_list)
#׼�������ݺͱ�ǩ�ͽ�VGG������
X_train=data
Y_train = keras.utils.to_categorical(image_label,4) #ת����one-hot����

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
############ע�⣺������������������࣬�������������������ԣ������ϱ��жϳ�͹�ۣ���һ����Ҫ����#################
s_pre_out='������ȱ������Ϊ��'+s_pre
s_true_out='��ʵȱ������Ϊ��'+s_true

print(s_pre_out)
print(s_true_out)

ttfront = ImageFont.truetype('simhei.ttf', 20)#�����С

draw.text((30,40),str(s_pre_out), fill = (255, 0 ,0), font=ttfront)
draw.text((50,60),str(s_true_out), fill = (255, 0 ,0), font=ttfront)

image.show()

from keras import backend as K
K.clear_session()
