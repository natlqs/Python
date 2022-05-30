# 将摄像头拍摄的图像存储至photo.jpg，同时将这个图像做识别处理，框出脸型，同时
# 将所框脸型存入faceout.jpg

import cv2
from PIL import Image


picpath = r"C:\Users\Natlqs1234\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\cv2\data\haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(picpath)       # 建立识别文件对象
cv2.namedWindow('Photo')
cap = cv2.VideoCapture(0)       # 开启摄像头
while(cap.isOpened()):       #如果摄像头打开就开启循环
    ret, img = cap.read()       # 读取图像
    cv2.imshow('Photo', img)        # 在OpenCv窗口显示图像
    if ret == True:         # 如果读取图像成功
        key = cv2.waitKey(200)          # 0.2秒检查一次
        if key == ord('a') or key == ord('A'):       # 如果按A或a
            cv2.imwrite('.\\python\\opencv\\Picture\\photo.jpg', img)       # 将图像写入photo.jpg
            break
cap.release()           # 关闭摄像头

faces = face_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20))
print(faces)

# 标注右下角底色是黄色
cv2.rectangle(img, (img.shape[1]-140, img.shape[0]-20),
                (img.shape[1], img.shape[0]), (0, 255, 255), -1)
                
# 标注找到多少人脸
cv2.putText(img, "Find" + str(len(faces)) + " face", 
            (img.shape[1]-140, img.shape[0]-5),
            cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 1)
            
# 将人脸框起来
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+y, w+h), (255, 0, 0), 2)       # 蓝色框住人脸
    myimg = Image.open(".\\python\\opencv\\Picture\\photo.jpg")   # PIL模块开启
    imgCrop = myimg.crop((x, y, x+w, y+h))      # 裁切
    imgResize = imgCrop.resize((150, 150), Image.ANTIALIAS)
    imgResize.save('.\\python\\opencv\\Picture\\FaceResult\\faceout.jpg')     # 存储文件

cv2.namedWindow("FaceRecognition", cv2.WINDOW_NORMAL)
cv2.imshow("FaceRecognition", img)
cv2.waitKey(20000)



