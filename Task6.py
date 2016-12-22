import cv2
import numpy as np

img = cv2.imread('messi.png', 0)
rows, cols = img.shape

M = np.float32([[1, 0, 10], [0, 1, 10]])
dst1 = cv2.warpAffine(img, M, (cols, rows))
rows, cols = dst1.shape
M = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 1)
dst = cv2.warpAffine(img, M, (cols, rows))
cv2.imshow('img', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

img = cv2.imread('messi.png', 0)
rows, cols = img.shape

