import numpy 
import cv2
import time
# Saving the video
cap = cv2.VideoCapture(0)
fourcc = cv2.cv.CV_FOURCC(*'XVID')
out = cv2.VideoWriter('Task2.avi',fourcc,25.0, (640,480))
start = time.time();
print start
end=0
while ((cap.isOpened() & (bool)(end <=5.000000000))):
	ret,frame = cap.read()
	if ret==True:
		frame = cv2.flip(frame,0)
		out.write(frame)
		cv2.imshow('frame',frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	else:
		break
	end = time.time() - start;
cap.release()
out.release()
