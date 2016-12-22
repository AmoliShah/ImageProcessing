import numpy 
import cv2
# Saving the video
cap = cv2.VideoCapture(0)
fourcc = cv2.cv.CV_FOURCC(*'XVID')
out = cv2.VideoWriter('output1.avi',fourcc,25.0, (640,480))
while (cap.isOpened()):
	ret,frame = cap.read()
	if ret==True:
		frame = cv2.flip(frame,0)
		out.write(frame)
		cv2.imshow('frame',frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	else:
		break
cap.release()
out.release()
