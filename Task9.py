import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread('opencv.png',0)
equ=cv2.equalizeHist(img)
res=np.hstack((img,equ))
cv2.imshow('hist',res)
plt.hist(img.ravel(),256,[0,256]); plt.show() #Plots Histogram plot
plt.hist(equ.ravel(),256,[0,256]); plt.show() #Plots Histogram plot
cv2.waitKey(0)
cv2.destroyAllWindows()