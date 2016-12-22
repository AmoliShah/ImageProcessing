import numpy as np
import cv2
cap = cv2.VideoCapture(0)
while(1):
	_, frame = cap.read()
	hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	l_b = np.array([110,50,50])
	h_b = np.array([130,255,255])
	mask = cv2.inRange(hsv,l_b,h_b)
	res = cv2.bitwise_and(frame,frame,mask = mask)
	cv2.imshow('frame',frame)
	cv2.imshow('res',res)
	cv2.imshow('mask',mask)
	k=cv2.waitKey(5) & 0xFF
	if k==27:
		break
cv2.destroyAllWindows()
