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
    mask_gray = cv2.inRange(hsv, color_range[0], color_range[1]) #色彩範圍二值化
    mask_rgb = cv2.cvtColor(mask_gray, cv2.COLOR_GRAY2RGB) #色彩空間轉換GRAY->RGB
    mask_list = mask_rgb.tolist() #將mask_rgb轉換成python的陣列(list)
    height, width, channels = mask_rgb.shape #取得mask_rgb的長寬
    #透過輪詢每個像素改變值
    for i in range(height):
        for j in range(width):
            if mask_list[i][j] != [255, 255, 255]:
                mask_list[i][j] = [0, 0, 0]
    mask = np.array(mask_list, dtype=frame.dtype) #將mask_list轉換成opencv圖像格式
    res = cv2.addWeighted(frame, 1, mask, 1, 0) #圖像融合
    cv2.imshow('1.frame', frame)
    cv2.imshow('2.mask', mask_rgb)
    cv2.imshow('3.res', res)
    if cv2.waitKey(1) & 0xFF == ord('q'): break #按Q跳出
cap.release()
cv2.destroyAllWindows()

