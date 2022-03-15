import cv2
import numpy as np

cap = cv2.VideoCapture(0) #讀取影片
glasses = cv2.imread('thug_life.jpg') #讀取照片
cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #載入特徵分類器

def chromaKey(backgroud, image, pos): #去背合成
    mask = cv2.inRange(image, (200, 200, 200), (255, 255, 255))
    mask_height, mask_width = mask.shape
    backgroud_height, backgroud_width, backgroud_channels = backgroud.shape
    for i in range(mask_height):
        for j in range(mask_width):
            if mask[i][j] == 0 and i+pos[1] < backgroud_height and j+pos[0] < backgroud_width:
                backgroud[i+pos[1],j+pos[0],:] = image[i,j,:]
    return backgroud

while True:
    ret, frame = cap.read()
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #色彩轉灰階
    faceRects = cascade.detectMultiScale(grey, scaleFactor = 1.35, minNeighbors = 3) #開始辨識
    for faceRect in faceRects: #依序框起來
        x, y, w, h = faceRect
        glasses_resize = cv2.resize(glasses, (w, h)) #縮放
        # cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        frame = chromaKey(frame.copy(), glasses_resize, (x, y))
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): break #按Q跳出
cap.release()
cv2.destroyAllWindows()





