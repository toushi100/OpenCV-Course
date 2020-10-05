import cv2 as cv
import numpy as np
#warping the image to give the right perspective (parallel to the camera)
img = cv.imread("card.jpg")
img = cv.resize(img,(400,600))
width , height = 400,300
points = np.float32([[47,421],[346,446],[318,291],[101,280]])
pointsmapping = np.float32([[0,height],[width,height],[width,0],[0,0]])
matrix = cv.getPerspectiveTransform(points,pointsmapping)
imgOutput = cv.warpPerspective(img,matrix,(width,height))
cv.imshow("Image", img)
cv.imshow("Image warpped", imgOutput)
cv.waitKey(0)