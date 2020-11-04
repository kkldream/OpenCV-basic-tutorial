import cv2 #引入函式庫
import numpy as np #引入函式庫
img = cv2.imread('road.jpg') #讀取圖片
print(img.shape)
cv2.imshow('img', img) #顯示圖片

light = np.uint8(np.clip((1.5 * img + 100), 0, 255)) #調亮
cv2.imshow('light', light)

grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #轉灰階
cv2.imshow('grey', grey)

kernel = np.array(( #浮雕
        [-2, -1, 0],
        [-1, 1, 1],
        [0, 1, 2]))
emboss = cv2.filter2D(grey, -1, kernel)
cv2.imshow('emboss', emboss)

kernel = np.array(( #垂直邊緣
        [1, 0, -1],
        [2, 0, -2],
        [1, 0, -1]))
edge_convolution = cv2.filter2D(grey, -1, kernel)
cv2.imshow('edge_convolution', edge_convolution)

edge = cv2.Canny(grey, 100, 200) #Canny邊緣檢測
cv2.imshow('edge', edge)

cv2.waitKey(0) #等待按下任意鍵
cv2.destroyAllWindows() #關閉所有視窗



