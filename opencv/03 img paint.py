# opencv img paint
import cv2
cv2.namedWindow('mypicture')       # 使用预设大小
img = cv2.imread('E:\VMcommunicate\CODE\python\opencv\OIP-C.jpg')  # 彩色读取
cv2.line(img, (10, 10), (220, 10),(255, 0, 0), 2)        # 输出线条
cv2.rectangle(img, (10, 50), (220, 90), (0, 0, 255), 2)      # 输出矩形
cv2.putText(img, "I like OpenCV", (30, 35), 
            cv2.FONT_ITALIC,1,  (0, 0, 255),3)
cv2.imshow('mypicture', img)      # 显示img
cv2.waitKey(30000)                   # 等待3秒
cv2.destroyAllWindows()             # 删除所有窗口
