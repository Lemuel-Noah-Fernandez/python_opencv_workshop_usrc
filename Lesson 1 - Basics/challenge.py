import cv2
import numpy as np

# Reading the image
img = cv2.imread('..\Photos\optical_illusion.jpg')
cv2.imshow('Opt', img)

# Allow d-key to kill the image
while True:
    #isTrue, frame = img.read()
    if cv2.waitKey(20) & 0xFF == ord('d'):
        break

# Resizing
def rescale(frame, scale=0.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv2.resize(frame, dimensions, interpolation = cv2.INTER_AREA)

rescaled = rescale(img, scale=0.5)
cv2.imshow('Half_size', rescaled)

# Drawing shapes
'''
blank = np.zeros((500, 500, 2), dtype='uint8')
rect = cv2.rectangle(img, (0, 0), (250, 250), (0, 0, 255), thickness=cv2.FILLED)
cv2.imshow('rectangle', rect)
'''
while True:
    #isTrue, frame = img.read()
    rect = cv2.imread('..\Photos\optical_illusion.jpg')
    cv2.rectangle(rect,(900,200),(250,250),(0,0,255),thickness=cv2.FILLED)
    if cv2.waitKey(20) & 0xFF == ord('d'):
        break

cv2.imshow('rectangle', rect)

# Passing through greyscale
greyscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grey', greyscale)

# Blur
blur=cv2.GaussianBlur(img,(11,11),cv2.BORDER_DEFAULT) 
cv2.imshow('Blur',blur)

# Canny
canny=cv2.Canny(img,125,200)
cv2.imshow('Canny',canny)

# Rotation
def rotate(img, angle, rotPoint=None):
    (height,width)=img.shape[:2]

    if rotPoint is None:
        rotPoint=(width//2,height//2)
    
    rotMat = cv2.getRotationMatrix2D(rotPoint,angle,scale=1.0)
    dimensions =(width,height)

    return cv2.warpAffine(img,rotMat,dimensions)

rotated= rotate(img,45)
cv2.imshow('Rotate', rotated)

# Waitkey
cv2.waitKey(0)