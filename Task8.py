import numpy as np
import cv2
img = cv2.imread('2.JPG')
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
im = cv2.drawContours(imgray,contours,3,(0,255,0),3)
maxarea = 0
for cnt in contours:
	 area = cv2.contourArea(cnt)
	 print area
	 if(area > maxarea):
	 	maxarea = area
print maxarea
# Finds all bounding rectangles
for cnt in contours:
	x,y,w,h = cv2.boundingRect(cnt)
	cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
cv2.imshow('img',imgray)
cv2.imshow('im',img)
cv2.waitKey(0)
cv2.destroyAllWindows()