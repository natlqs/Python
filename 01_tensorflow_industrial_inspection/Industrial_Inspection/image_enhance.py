from keras.preprocessing.image import ImageDataGenerator
import numpy as np
import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.optimizers import SGD
import tensorflow as tf
from PIL import Image
from image_handle import *
import os
import cv2


batch_size=10
epoch_size=50
data = np.empty((250,800, 800,3), dtype="float32")
image_resize=[]
image_vector=[]
image_label=[]
image_label_list=['����','©��','����','͹��']  #©��ռ�ı���̫���ˣ����º����Ԥ��ȫ����ƫ�������
image_dir='F:/Data/guangdong_round1_train1_20180903/'
j=0
k=0

for fn in os.listdir(image_dir):
    image_name=get_image_name(fn)
    for i in range(0,4):
        if image_label_list[i]==image_name:
            image_name=i
    image = Image.open(image_dir+fn,'r')#ԭʼͼƬ����
    image_down=image.resize((800, 800), Image.ANTIALIAS)
    arr = np.asarray(image_down, dtype="float32")
    data[j, :, :, :] = arr
    j=j+1
    image_label.append(image_name)

#׼�������ݺͱ�ǩ�ͽ�VGG������
x_train=data[231:250]
y_train = keras.utils.to_categorical(image_label,4)[231:250]#ת����one-hot����

print(len(x_train))
print(len(y_train))
print(image_label)

generator = ImageDataGenerator(
        rotation_range=20,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.1,
        zoom_range=0.1,
        horizontal_flip=True,
    )

for batch in generator.flow(x_train,
                          batch_size=100,
                          save_to_dir='C:/Users/18301/Desktop/image_data',#���ɺ��ͼ�񱣴�·��
                          save_prefix='����2018',
                          save_format='jpg'):
    k += 1
    if k > 10: #���10ָ��Ҫ�������ٸ����ݣ����յ�����Ϊx_train�Ĵ�С��10�ĳ˻����ɸ���Ҫ�����и���
        break  # otherwise the generator would loop indefinitely
