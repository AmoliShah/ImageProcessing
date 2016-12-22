import cv2
import numpy as np
from matplotlib import pyplot as plt
cap = cv2.VideoCapture(0)
temp=cv2.imread('amoliHand.png',0)
while (True):
	ret,frame = cap.read()
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	w, h=temp.shape[::-1]
	method=cv2.TM_CCOEFF
	res = cv2.matchTemplate(gray,temp,method)
	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
	top_left = max_loc
	bottom_right = (top_left[0] + w, top_left[1] + h)
	cv2.rectangle(frame,top_left, bottom_right, 255, 2)
	plt.subplot(121),plt.imshow(res,cmap = 'gray')
	plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
	plt.subplot(122),plt.imshow(frame,cmap = 'gray')
	plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
	plt.show()
	if cv2.waitKey(0) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllindows()