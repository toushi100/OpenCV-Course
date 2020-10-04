import cv2
import numpy as np

img = cv2.imread("image.jpg")
print(img.shape)
img = cv2.resize(img,(400,600))
cv2.imshow("Rrsized Image", img)




# Cropping an Image
imgCrop = img[150:300,100:200]
cv2.imshow("Cropped Image", imgCrop)

cv2.waitKey(7000)