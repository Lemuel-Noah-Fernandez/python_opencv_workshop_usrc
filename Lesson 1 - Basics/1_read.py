import cv2
import numpy

#reading images

img = cv2.imread('..\Photos\cat.jpg')
cv2.imshow('Cat', img)

'''
# reading videos

capture = cv2.VideoCapture('..\Videos\dog.mp4')
#capture = cv2.VideoCapture(0)
#VideoCapture(0) = Webcam input

#capture=cv2.VideoCapture(0)

while True:
    isTrue,frame=capture.read()
    cv2.rectangle(frame,(900,200),(250,250),(0,0,255),thickness=cv2.FILLED)
    #show frame
    cv2.imshow('img',frame)

    #if the d key is pressed, kill screen
    if cv2.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv2.destroyAllWindows()
'''
cv2.waitKey(0)
