""" Experiment with face detection and image filtering using OpenCV """

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
kernel = np.ones((21,21),'uint8')


while(True):
	# Capture frame-by-frame
	ret, frame = cap.read()
	faces = face_cascade.detectMultiScale(frame, scaleFactor=1.2, minSize=(20,20))
	for (x,y,w,h) in faces:
		frame[y:y+h,x:x+w,:] = cv2.dilate(frame[y:y+h,x:x+w,:], kernel)
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255))
		#cv2.ellipse(frame, (int(x+w/2), int(y+2*h/3)), int(w/4), 0, 4, -4, (0,0,255))
		cv2.line(frame, (x+w/3, y+2*h/3), (x+2*w/3, y+2*h/3), (0,0,255))
		cv2.circle(frame, (x+w/3, y+h/3),w/15, (255, 255, 255), -1)
		cv2.circle(frame, (x+2*w/3, y+h/3),w/15, (255, 255, 255), -1)
		cv2.circle(frame, (x+w/3, y+h/3),w/30, (0, 0, 0), -1)
		cv2.circle(frame, (x+2*w/3, y+h/3),w/30, (0, 0, 0), -1)


	# Display the resulting frame
	cv2.imshow('frame', frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()