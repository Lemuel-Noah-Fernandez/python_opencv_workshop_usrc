import cv2
import numpy as np

img =cv2.imread('..\Photos/park.jpg')

cv2.imshow('Park',img)

#translation
def translate(img,x,y):
    # -x = Left
    # -y = Up
    transMat =np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])

    return cv2.warpAffine(img,transMat,dimensions)


translated = translate(img,100,100)
cv2.imshow('translated',translated)

#Rotation
def rotate(img, angle, rotPoint=None):
    (height,width)=img.shape[:2]

    if rotPoint is None:
        rotPoint=(width//2,height//2)
    
    rotMat = cv2.getRotationMatrix2D(rotPoint,angle,scale=3.0)
    dimensions =(width,height)

    return cv2.warpAffine(img,rotMat,dimensions)

rotated= rotate(img,-45)
cv2.imshow('Rotate',rotated)


#flipping
flip=cv2.flip(img,-1)
#-1 flips vertically and horizonatally 

'''
 A flag to specify how to flip the array; 
 0 means flipping around the x-axis and 
 positive value (for example, 1) means 
 flipping around y-axis. Negative value
  (for example, -1) means flipping around 
  both axes.
'''

#cropping 
cropped = img[200:400,200:400]
cv2.imshow('lol', flip)
cv2.imshow('cropped', cropped)

cv2.waitKey(0)