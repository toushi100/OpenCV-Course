import cv2 as cv
import numpy as np
from Stackimages import stackImages


# Contour and Shape detection
def getContours(img):
    contours, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv.contourArea(cnt)
        print(area)
        if area > 500:
            cv.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            peri = cv.arcLength(cnt, True)
            print(peri)
            approx = cv.approxPolyDP(cnt, 0.02 * peri, True)
            objcor = len(approx)
            print(objcor)
            x, y, w, h = cv.boundingRect(approx)

            if objcor == 3:
                objectType = "triangle"
            elif objcor == 4:
                aspRatio = w / float(h)
                if aspRatio > 0.98 & aspRatio < 1.03:
                    objectType = "Square"
                else:
                    objectType = "Rectangle"
            elif objcor > 4:
                objectType = "circle"
            else:
                objectType = "THAT'S NOT EVEN A SHAPE !!! WHAT IS THAT"

            cv.rectangle(imgContour, (x, y), (x + w, y + h), (0, 0, 0), 2)
            cv.putText(imgContour, objectType, (x + (w // 2) - 10, y + (h // 2) - 10), cv.FONT_HERSHEY_COMPLEX, 0.7,
                       (0, 0, 0), 2)


img = cv.imread("shapes.jpg")
img = cv.resize(img, (700, 900))
imgContour = img.copy()
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
imgBlur = cv.GaussianBlur(img, (21, 21), 1)
imgCanny = cv.Canny(img, 50, 50)
getContours(imgCanny)
imgBlank = np.zeros_like(img)
imgStack = stackImages(0.6, ([img, imgGray, imgBlur], [imgCanny, imgContour, imgBlank]))
cv.imshow("Stack", imgStack)
cv.waitKey(0)
