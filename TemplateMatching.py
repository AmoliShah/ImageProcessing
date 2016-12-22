import cv2
import numpy as np
from matplotlib import pyplot as plt
im1=cv2.imread('messi.png')
im2=cv2.cvtColor(im1,cv2.COLOR_BGR2GRAY)
temp=cv2.imread('messi_face.jpg',0)
w, h=temp.shape[::-1]
method=cv2.TM_CCOEFF
res = cv2.matchTemplate(im2,temp,method)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)
cv2.rectangle(im1,top_left, bottom_right, 255, 2)
plt.subplot(121),plt.imshow(res,cmap = 'gray')
plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(im1,cmap = 'gray')
plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
plt.show()
