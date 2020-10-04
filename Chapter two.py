import cv2
import numpy as np

img = cv2.imread("image.jpg")
kernel = np.ones((5,5),np.uint8)
#converting image to gray scale
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgGray = cv2.resize(imgGray,(400,600))
cv2.imshow("Gray Image", imgGray)


#adding blur to image
imgBlur = cv2.GaussianBlur(img,(255,255),0)
imgBlur = cv2.resize(imgBlur,(400,600))
cv2.imshow("Blured Image", imgBlur)

#image edge detection
imgCanny = cv2.Canny(img,70,100)
imgCanny = cv2.resize(imgCanny,(400,600))
cv2.imshow("Canny Image", imgCanny)


#image dilation
imgDilation = cv2.dilate(imgCanny,kernel,iterations=2)
imgDilation = cv2.resize(imgDilation,(400,600))
cv2.imshow("Dilation Image", imgDilation)

#image erosion
imgErosion = cv2.erode(imgDilation,kernel,iterations=1)
imgErosion = cv2.resize(imgErosion,(400,600))
cv2.imshow("Erosion Image", imgErosion)


cv2.waitKey(7000)