import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread('lenalow.jpg',0)
plt.hist(img.ravel(),256,[0,256]); plt.show()
equ=cv2.equalizeHist(img)
res=np.hstack((img,equ))
cv2.imshow('hist',res)
#plt.hist(equ.ravel(),256,[0,256]); plt.show() #Plots Histogram Equalized plot

cv2.waitKey(0)
cv2.destroyAllWindows()

