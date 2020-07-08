import cv2 #引入函式庫
img = cv2.imread('dog.jpg') #讀取圖片
cv2.imshow('img_original', img) #顯示圖片

img_resize = cv2.resize(img, (300, 300)) #縮放
cv2.imshow('img_resize', img_resize)

img_flip = cv2.flip(img, 1) #水平鏡像
cv2.imshow('img_flip', img_flip)

img_crop = img[100:200, 150:350] #裁切
cv2.imshow('img_crop', img_crop)

cv2.waitKey(0) #等待按下任意鍵
cv2.destroyAllWindows() #關閉所有視窗



