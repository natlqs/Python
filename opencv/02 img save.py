# opencv save img
import cv2
cv2.namedWindow('mypicture1')       # 使用预设大小
img1 = cv2.imread('E:\VMcommunicate\CODE\python\opencv\OIP-C.jpg')  # 彩色读取
cv2.imshow('mypicture1', img1)
cv2.imwrite('E:\VMcommunicate\CODE\python\opencv\out1.jpg', img1)
cv2.waitKey(3000)
cv2.destroyAllWindows()