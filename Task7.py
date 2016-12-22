import numpy as np
import cv2
cap = cv2.VideoCapture(0)
pixels = 0;
while(1):
	_, frame = cap.read()
	hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	l_y = np.array([20,100,100])
	h_y = np.array([30,255,255])
	mask = cv2.inRange(hsv,l_y,h_y)
	res = cv2.bitwise_and(frame,frame,mask = mask)
	if res.any() == True:
		pixels = pixels + 1;
	if pixels >=1000:
		print("Yellow color detected")
		print pixels
	cv2.imshow('frame',frame)
	cv2.imshow('res',res)
	cv2.imshow('mask',mask)
	k=cv2.waitKey(5) & 0xFF
	if k==27:
		break
cv2.destroyAllWindows()