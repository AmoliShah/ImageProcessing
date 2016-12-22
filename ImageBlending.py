import numpy
import cv2
im1 = cv2.imread('messi.png',0)
im2 = 255-im1
dat = cv2.addWeighted(im1,0.7,im2,0.3,0)
cv2.imshow('im1',im1)
cv2.imshow('im2',im2)
cv2.imshow('dat',dat)
cv2.waitKey(0)
cv2.destroyAllWindows();