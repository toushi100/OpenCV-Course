import cv2 as cv
import numpy as np
from Stackimages import stackImages

faceCascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
img = cv.imread("image.jpg")
img = cv.resize(img,(400,600))
imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Vertical Image", imgGray)

faces = faceCascade.detectMultiScale(imgGray,1.1,4)
for (x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,0,0),4)


cv.waitKey(0)