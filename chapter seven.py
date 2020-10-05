import cv2 as cv
import numpy as np

#color detection and manipulation

def empty(a):
    pass
def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv.cvtColor( imgArray[x][y], cv.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv.cvtColor(imgArray[x], cv.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver


cv.namedWindow("TrackBars")
cv.resizeWindow("TrackBars", 400,600)
cv.createTrackbar("hue min","TrackBars",0,179,empty)
cv.createTrackbar("hue max","TrackBars",179,179,empty)
cv.createTrackbar("sat min","TrackBars",0,255,empty)
cv.createTrackbar("sat max","TrackBars",255,255,empty)
cv.createTrackbar("val min","TrackBars",0,255,empty)
cv.createTrackbar("val max","TrackBars",255,255,empty)

while True:
    img = cv.imread("card.jpg")
    img = cv.resize(img,(400,600))
    imgHSV = cv.cvtColor(img,cv.COLOR_BGR2HSV)
    H_min = cv.getTrackbarPos("hue min", "TrackBars")
    H_max = cv.getTrackbarPos("hue max", "TrackBars")
    S_min = cv.getTrackbarPos("sat min","TrackBars")
    S_max = cv.getTrackbarPos("sat max","TrackBars")
    V_min = cv.getTrackbarPos("val min","TrackBars")
    V_max = cv.getTrackbarPos("val max","TrackBars")
    print(H_min,H_max,S_min,S_max,V_min,V_max)
    lower = np.array([H_min,S_min,V_min])
    upper = np.array([H_max,S_max,V_max])
    mask = cv.inRange(imgHSV,lower,upper)
    imgResult = cv.bitwise_and(img,img,mask=mask)

    imgStack = stackImages(0.6, ([img, imgHSV], [mask, imgResult]))
    cv.imshow("Stacked Images", imgStack)
    cv.waitKey(1)


