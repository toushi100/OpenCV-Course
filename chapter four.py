import cv2
import numpy as np
img = np.zeros((1000,1000,3),np.uint8)
img2 = np.zeros((1000,1000,3),np.uint8)
print(img.shape)
img[:] = 200,146,165
img2[100:300,100:300] = 50,146,165
cv2.line(img2,(0,0),(img.shape[1],img.shape[0]),(255,255,255),6)
cv2.rectangle(img,(150,150),(300,300),(90,90,90),5)
cv2.circle(img,(256,256),70,(200,200,200),7)
cv2.putText(img2,"OPEN CV",(100,100),cv2.FONT_HERSHEY_COMPLEX,2,(42,63,123),6)
cv2.imshow("Cropped Created Image",img2)
cv2.imshow("Created Image",img)

cv2.waitKey(8000)