import cv2 #引入函式庫

img = cv2.imread('dog.jpg') #讀取圖片
print(img.shape)

for i in [(10, 20), (510, 20), (10, 580), (500, 580)]:
    #cv2.putText(影像, 文字, 座標, 字型, 大小, 顏色, 線條寬度, 線條種類)
    cv2.putText(img, str(i), i, cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 0, 0), 1, cv2.LINE_AA)

#cv2.line(影像, 開始座標, 結束座標, 顏色, 線條寬度)
cv2.line(img, (300, 100), (500, 500), (0, 0, 255), 3)

#cv2.rectangle(影像, 頂點座標, 對向頂點座標, 顏色, 線條寬度)
cv2.rectangle(img, (20, 60), (120, 160), (0, 255, 0), 2)
cv2.rectangle(img, (140, 180), (200, 240), (0, 255, 0), -1)

#cv2.circle(影像, 圓心座標, 半徑, 顏色, 線條寬度)
cv2.circle(img,(300, 410), 30, (0, 255, 255), 3)
cv2.circle(img,(390, 410), 15, (255, 0, 0), -1)

cv2.imshow('dog', img) #顯示圖片

cv2.waitKey(0) #等待按下任意鍵
cv2.destroyAllWindows() #關閉所有視窗