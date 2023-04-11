import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten,Input
from keras.layers import Conv2D, MaxPooling2D,merge
from keras.layers import BatchNormalization,Activation
from sklearn.model_selection import train_test_split
from keras.optimizers import SGD
from keras import regularizers
from keras.models import Model
import tensorflow as tf
from PIL import Image
from image_handle import *
import os
import cv2


class BuildModel():

    def __init__(self,x_train,y_train,x_test,y_test,batch_size,epoch_size):
        self.x_train=x_train
        self.y_train = y_train
        self.x_test=x_test
        self.y_test=y_test
        self.batch_size=batch_size
        self.epoch_size=epoch_size

    def add_layer(self,X,channel_num):
        #借鉴残差网络的思想
        conv_1=Conv2D(channel_num, (3, 3),padding='same')(X)
        conv_1=BatchNormalization()(conv_1)
        conv_1= Activation('relu')(conv_1)
        # conv_1 = MaxPooling2D(pool_size=(3, 3),strides=(1,1),padding='same')(conv_1)
        conv_1 = Conv2D(channel_num, (3, 3),padding='same')(conv_1)
        conv_1 = BatchNormalization()(conv_1)
        merge_data = merge([conv_1, X], mode='sum')
        out = Activation('relu')(merge_data)
        return out

    def google_layer(self,X):
        #借鉴GoogleNet的思想,单层分支
        conv_1 = Conv2D(32,(1, 1), padding='same')(X)
        conv_1 = BatchNormalization()(conv_1)
        conv_1 = Activation('relu')(conv_1)
        conv_2 = Conv2D(32,(3, 3), padding='same')(X)
        conv_2 = BatchNormalization()(conv_2)
        conv_2 = Activation('relu')(conv_2)
        conv_3 = Conv2D(32,(5, 5), padding='same')(X)
        conv_3 = BatchNormalization()(conv_3)
        conv_3 = Activation('relu')(conv_3)
        pooling_1 = MaxPooling2D(pool_size=(2, 2), strides=(1, 1), padding='same')(X)
        out = merge([conv_1,conv_2,conv_3,pooling_1], mode='concat')
        return out

    def run_model(self):
        # input: 100x100 images with 3 channels -> (100, 100, 3) tensors.
        # this applies 32 convolution filters of size 3x3 each.
        #在这里采用函数式模型不采用序贯式模型
        #发现单纯使用残差网络比使用残差+GoogleNet效果要好，收敛速度更快
        inputs=Input(shape=(300,300,3))
        X=Conv2D(32, (3, 3))(inputs)
        X=BatchNormalization()(X)
        X=Activation('relu')(X)
        X=self.add_layer(X,32)
        # X=self.google_layer(X)
        X=MaxPooling2D(pool_size=(2, 2),strides=(2,2))(X)
        X=Conv2D(64, (3, 3),kernel_regularizer=regularizers.l2(0.01))(X)
        X=BatchNormalization()(X)
        X=Activation('relu')(X)
        X=self.add_layer(X,64)
        # X = self.google_layer(X)
        X = MaxPooling2D(pool_size=(2, 2), strides=(2, 2))(X)
        X=Conv2D(64, (3, 3))(X)
        X=BatchNormalization()(X)
        X=Activation('relu')(X)
        X=MaxPooling2D(pool_size=(2, 2),strides=(2,2))(X)
        X = self.add_layer(X, 64)
        # X = self.google_layer(X)
        X=Conv2D(32, (3, 3),kernel_regularizer=regularizers.l2(0.01))(X)
        X=BatchNormalization()(X)
        X=Activation('relu')(X)
        X=self.add_layer(X,32)
        # X = self.google_layer(X)
        X = MaxPooling2D(pool_size=(2, 2), strides=(2, 2))(X)
        X=Conv2D(64, (3, 3))(X)
        X=BatchNormalization()(X)
        X=Activation('relu')(X)
        X=self.add_layer(X,64)
        # X = self.google_layer(X)
        X=Flatten()(X)
        X=Dense(256, activation='relu')(X)
        X=Dropout(0.5)(X)
        predictions=Dense(4, activation='softmax')(X)
        model = Model(inputs=inputs, outputs=predictions)
        # sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
        model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
        model.fit(self.x_train, self.y_train, batch_size=self.batch_size, epochs=self.epoch_size, class_weight = 'auto',validation_split=0.1)
        model.save('model_google_layer.h5')
        score = model.evaluate(self.x_test, self.y_test, batch_size=self.batch_size)
        print(score)

