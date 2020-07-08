import cv2
import numpy as np
color_range = [np.array([35, 0, 0]), np.array([77, 255, 255])] #顏色範圍
cap = cv2.VideoCapture('green.mp4') #讀取影片
while True:
    ret, frame = cap.read()
    if ret == False: #如果影片沒下一幀
        cap = cv2.VideoCapture('green.mp4') #重新讀取影片
        ret, frame = cap.read() #補前面沒讀到的一幀
    crop = frame[150:250, 160:854] #裁切
    draw = np.ones((crop.shape[0],crop.shape[1],3), np.uint8)
    hsv = cv2.cvtColor(crop, cv2.COLOR_BGR2HSV) #色彩空間轉換BGR->HSV
    mask = cv2.inRange(hsv, color_range[0], color_range[1]) #色彩範圍二值化
    for i in range(mask.shape[0]):
        for j in range(mask.shape[1]):
            if mask[i][j] == 0: draw[i,j,:] = crop[i,j,:] #黑色部分還原
            else: draw[i,j,:] = 200 #白色部分當背景
#    cv2.imshow('0.frame', frame)
    cv2.imshow('1.crop', crop)
    cv2.imshow('2.mask', mask)
    cv2.imshow('3.draw', draw)
    if cv2.waitKey(30) & 0xFF == ord('q'): break #按Q跳出
cap.release()
cv2.destroyAllWindows()

