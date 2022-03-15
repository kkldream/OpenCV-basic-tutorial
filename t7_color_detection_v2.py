import cv2
import numpy as np
color_range = (35, 0, 0), (77, 255, 255) #顏色範圍
cap = cv2.VideoCapture('國動5個綠幕去背.mp4') #讀取影片
while True:
    ret, frame = cap.read()
    if ret == False: #如果影片沒下一幀
        cap = cv2.VideoCapture('國動5個綠幕去背.mp4') #重新讀取影片
        ret, frame = cap.read() #補前面沒讀到的一幀
    frame = cv2.resize(frame, (432, 240))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #色彩空間轉換BGR->HSV
    mask = cv2.inRange(hsv, color_range[0], color_range[1]) #色彩範圍二值化
    mask_rgb = cv2.cvtColor(mask, cv2.COLOR_GRAY2RGB) #色彩空間轉換GRAY->RG
    b_channel, g_channel, r_channel = cv2.split(mask_rgb) #分割rgb通道
    # 使用cv2.threshold函数，输入BRG三个通道的灰度图像，和触发阈值，和转换值，还有触发器类型
    ret1, b = cv2.threshold(b_channel, 1, 255, cv2.THRESH_BINARY)
    ret2, g = cv2.threshold(g_channel, 1, 255, cv2.THRESH_BINARY)
    ret3, r = cv2.threshold(r_channel, 1, 255, cv2.THRESH_BINARY)
    dst = cv2.merge((b,g,r)) #合併rgb通道為單一圖檔
    res = cv2.addWeighted(frame, 1, dst, 1, 0)
    cv2.imshow('1.frame', frame)
    cv2.imshow('2.mask', mask)
    cv2.imshow('3.res', res)
    if cv2.waitKey(30) & 0xFF == ord('q'): break #按Q跳出
cap.release()
cv2.destroyAllWindows()

