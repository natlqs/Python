# face recognition and face save
import cv2
from PIL import Image as pilImage
import tkinter as tk
from tkinter import Image, filedialog

root = tk.Tk()
root.withdraw()

pic_path = r"C:\Users\natlq\AppData\Local\Programs\Python\Python310\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(pic_path)      # 建立识别文件对象
img_path = filedialog.askopenfilename()
img = cv2.imread(img_path)      # 读取图像文件建立图像文件对象
faces = face_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors = 3, minSize=(20, 20))
# 标注右下角底色是黄色
cv2.rectangle(img, (img.shape[1]-140, img.shape[0]-20),
            (img.shape[1], img.shape[0]), (0, 255, 255), -1)
# 标注找到多少人脸
cv2.putText(img, 'finding' + str(len(faces)) + 'faces',
            (img.shape[1]-135, img.shape[0]-5),
            cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 1)
# 将人脸框起来，有于有可能找到好几个脸所以用循环绘出来
num = 1
for(x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    filename0 = '.\\python\\opencv\\Picture\\FaceResult\\face' + str(num) + '.jpg'           # 建立文件名
    image = pilImage.open(img_path)                    # PIL模块开启
    imageCrop = image.crop((x, y, x+w, y + h))      # 裁剪
    imageResize = imageCrop.resize((150, 150), pilImage.ANTIALIAS) # 高质量重制大小
    imageResize.save(filename0)      # 存储大小
    num += 1            # 文件编号
cv2.namedWindow('face', cv2.WINDOW_NORMAL)      # 建立图像对象
cv2.imshow('face', img)     # 显示图像
cv2.waitKey(30000)
cv2.destroyAllWindows()

