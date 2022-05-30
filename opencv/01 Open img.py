<<<<<<< HEAD
import cv2
cv2.namedWindow('mypicture1')       # 使用预设大小
cv2.namedWindow('mypicture2', cv2.WINDOW_NORMAL)       # 可以重设大小
img1 = cv2.imread('./python/opencv/Picture/OIP-C.jpg')  # 彩色读取
img2 = cv2.imread('./python/opencv/Picture/OIP-C.jpg', 0)  #    灰色读取 
cv2.imshow('mypicture1', img1)      # 显示img1
cv2.imshow('mypicture2', img2)      # 显示img2
cv2.waitKey(3000)                   # 等待3秒
cv2.destroyWindow('mypicture1')         # 删除Mypicture1
cv2.waitKey(3000)                   # 等待3秒
=======
import cv2
cv2.namedWindow('mypicture1')       # 使用预设大小
cv2.namedWindow('mypicture2', cv2.WINDOW_NORMAL)       # 可以重设大小
img1 = cv2.imread('E:\VMcommunicate\CODE\python\opencv\OIP-C.jpg')  # 彩色读取
img2 = cv2.imread('E:\VMcommunicate\CODE\python\opencv\OIP-C.jpg', 0)  #    灰色读取 
cv2.imshow('mypicture1', img1)      # 显示img1
cv2.imshow('mypicture2', img2)      # 显示img2
cv2.waitKey(3000)                   # 等待3秒
cv2.destroyWindow('mypicture1')         # 删除Mypicture1
cv2.waitKey(3000)                   # 等待3秒
>>>>>>> 459e0039b53f6ddbd771be8854151f6747232b26
cv2.destroyAllWindows()             # 删除所有窗口