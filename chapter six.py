import cv2 as cv
import numpy as np

# Vertical and Horizontal stacking of two different images
img = cv.imread("image.jpg")
img2 = cv.imread("card.jpg")
img = cv.resize(img,(400,600))
img2 = cv.resize(img2,(400,600))
verticalStack = np.vstack((img2,img))
horizontalStack = np.hstack((img2,img))
cv.imshow("Horizontal Image", horizontalStack)
cv.imshow("Vertical Image", verticalStack)



cv.waitKey(0)