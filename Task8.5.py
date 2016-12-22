import numpy as np
import cv2
from matplotlib import pyplot as plt
im1 = cv2.imread('messi.png',0)
im2 = 255-im1
dat = cv2.addWeighted(im1,0.7,im2,0.3,0)
cv2.imshow('dat',dat)
equ=cv2.equalizeHist(dat)
res=np.hstack((dat,equ))
cv2.imshow('hist',res)
plt.hist(equ.ravel(),256,[0,256]); plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()