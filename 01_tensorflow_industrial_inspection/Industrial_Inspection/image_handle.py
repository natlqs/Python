import numpy as np
from PIL import Image
import random
import re
import os

def get_image_name(image_name):
    image_name=re.split('.jpg', image_name)
    name=re.split('2018',image_name[0])
    return name[0]

def one_hot_vector(image_label,image_label_list):
    classes=len(image_label_list)
    one_hot_label = np.zeros(shape=(image_label.shape[0], classes+1))  ##生成全0矩阵
    one_hot_label[np.arange(0, image_label.shape[0]), image_label] = 1
    return one_hot_label

def batch_generate(x_train,y_train,batch_size):
    batch_x=[]
    batch_y=[]
    for i in range(batch_size):
        t = random.randint(0, 249)
        batch_x.append(x_train[t])
        batch_y.append(y_train[t])
    return batch_x,batch_y

def get_image_data(image_dir,resize_width,resize_height,data,image_label,image_label_list):
    j=0
    image_vec=[]
    for fn in os.listdir(image_dir):
        image_name = get_image_name(fn)
        for i in range(0, 4):
            if image_label_list[i] == image_name:
                image_name = i
        image = Image.open(image_dir + fn)  # 原始图片过大
        image_down = image.resize((resize_width,resize_height), Image.ANTIALIAS)
        image_vec.append(image_down)
        arr = np.asarray(image_down, dtype="float32")
        data[j, :, :, :] = arr
        j = j + 1
        image_label.append(image_name)
    return data,image_label,image_vec



