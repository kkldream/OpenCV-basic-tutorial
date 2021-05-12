import cv2

cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #載入特徵分類器

img = cv2.imread('face.jpg') #讀取照片

grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #色彩轉灰階
faceRects = cascade.detectMultiScale(grey, scaleFactor = 1.3, minNeighbors = 5) #開始辨識
for faceRect in faceRects: #依序框起來
    x, y, w, h = faceRect        
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv2.imshow('Haar', img) #顯示照片

cv2.waitKey(0)
cv2.destroyAllWindows()