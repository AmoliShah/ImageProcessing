import numpy as np;
import cv2

img = cv2.imread('messi.png',0)
cv2.namedWindow('image')
cv2.resizeWindow('image', 540,480)
cv2.imshow('image',img)
if cv2.waitKey(0)==27:
	cv2.destroyAllWindows()
else:
	cv2.imwrite('File1.png',img)

