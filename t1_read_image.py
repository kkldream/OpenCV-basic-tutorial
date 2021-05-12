import cv2 #引入函式庫

img = cv2.imread('thug_life.png', cv2.IMREAD_UNCHANGED) #讀取圖片
print(img.shape)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if img[i][j][3] != 0: img[i][j] = (255, 0, 0, 255) #黑色部分還原
cv2.imshow('img_original', img) #顯示圖片

cv2.waitKey(0) #等待按下任意鍵
cv2.destroyAllWindows() #關閉所有視窗