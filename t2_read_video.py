import cv2
import time

cap = cv2.VideoCapture("move.mp4") #讀取影片

while True:
    ret, frame = cap.read() #讀取每一幀
    cv2.imshow('frame', frame)
    time.sleep(0.01)
    if cv2.waitKey(1) & 0xFF == ord('q'): break #按Q跳出
    
cap.release()
cv2.destroyAllWindows()