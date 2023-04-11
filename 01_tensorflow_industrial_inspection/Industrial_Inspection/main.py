import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import BatchNormalization,Activation
from sklearn.model_selection import train_test_split
from keras.optimizers import SGD
import tensorflow as tf
from PIL import Image
from image_handle import *
from model import BuildModel
import os
import cv2
import keras.backend.tensorflow_backend as KTF

#进行配置，使用60%的GPU,这是为了保护GPU
config = tf.ConfigProto()
config.gpu_options.per_process_gpu_memory_fraction = 0.6
session = tf.Session(config=config)
# 设置session
KTF.set_session(session )

batch_size=5
epoch_size=50
image_number=1451
resize_width=300
resize_height=300

image_vec=[]
image_resize=[]
image_vector=[]
image_label=[]
image_label_list=['擦花','漏底','碰凹','凸粉']  #漏底占的比例太大了，导致后面的预测全部都偏向该物体
data = np.empty((1429,300, 300,3), dtype="float32")
image_dir='F:/Data/guangdong_round1_train1_20180903/image_data/'

data,image_label,image_vec=get_image_data(image_dir,resize_width,resize_height,data,image_label,image_label_list)
#准备好数据和标签送进VGG网络中
X_train=data
Y_train = keras.utils.to_categorical(image_label,4) #转换成one-hot向量
#划分训练集和测试集
x_train, x_test,y_train, y_test = train_test_split(X_train, Y_train,test_size=0.1, random_state=None)
#开始建立序列模型
model=BuildModel(x_train,y_train,x_test,y_test,batch_size,epoch_size)
model.run_model()