import cv2 #引入函式庫
import numpy as np #引入函式庫

cap = cv2.VideoCapture(0) #讀取影片

while True:
	ret, frame = cap.read() #讀取每一幀
	
	cv2.imshow('img', frame) #顯示圖片

	light = np.uint8(np.clip((1.5 * frame + 100), 0, 255)) #調亮
	cv2.imshow('light', light)

	grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #轉灰階
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

	if cv2.waitKey(1) & 0xFF == ord('q'): break #按Q跳出

cap.release()
cv2.destroyAllWindows() #關閉所有視窗