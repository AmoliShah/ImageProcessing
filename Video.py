import numpy 
import cv2

cap = cv2.VideoCapture(0)
while (True):
	ret,frame = cap.read()
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)  #to convert color frames to gray frames
	cv2.imshow('frame',gray)
	if cv2.waitKey(100) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllindows()