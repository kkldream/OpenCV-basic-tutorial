import cv2
import numpy as np
def chromaKey(backgroud, image, pos, color): #去背合成
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, color[0], color[1])
    for i in range(mask.shape[0]):
        for j in range(mask.shape[1]):
            for p in pos:
                if mask[i][j] == 0 and i+p[1] < backgroud.shape[0] and j+p[0] < backgroud.shape[1]:
                    backgroud[i+p[1],j+p[0],:] = image[i,j,:]
    return backgroud
face = cv2.imread('face.jpg') #讀取照片
cap = cv2.VideoCapture('green.mp4') #讀取影片
cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #載入特徵分類器
color = [np.array([35, 0, 0]), np.array([77, 255, 255])] #顏色範圍
face = cv2.resize(face, (738, 500)) #縮放
grey = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY) #色彩轉灰階
faceRects = cascade.detectMultiScale(grey, scaleFactor = 1.35, minNeighbors = 2) #開始辨識
pos = []
for faceRect in faceRects: #依序框起來
    x, y, w, h = faceRect
    #cv2.rectangle(face, (x, y), (x + w, y + h), (255, 0, 0), 2)
    pos.append([x - 30, y + int(h / 3)]) #存座標
while True:
    ret, frame = cap.read()
    if ret == False: #如果影片沒下一幀
        cap = cv2.VideoCapture('green.mp4') #重新讀取影片
        ret, frame = cap.read() #補前面沒讀到的一幀
    crop = frame[150:250, 160:854] #裁切
    crop = cv2.resize(crop, (300, 40)) #縮放
    out = chromaKey(face.copy(), crop, pos, color) #引用函式
    cv2.imshow('out', out)
    if cv2.waitKey(1) & 0xFF == ord('q'): break #按Q跳出
cap.release()
cv2.destroyAllWindows()





