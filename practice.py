import cv2

# 馬賽克函式
# input:
# img: 輸入圖像
# bbox: 座標位置(x, y, w, h)，必須為整數
# size: 馬賽克程度
# output: 輸出圖像
def mosaic_effect(img, bbox, size=10):
    x, y, w, h = bbox
    new_img = img.copy()
    for m in range(y, y+h):
      for n in range(x, x+w):
          if m % size == 0 and n % size == 0:
            for i in range(0, size):
                for j in range(0, size):
                  (b, g, r) = new_img[m, n]
                  new_img[i + m, j + n] = (b, g, r)
    return new_img

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

