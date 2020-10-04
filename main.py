import cv2
#Importing and displaying an image
print("Package Imported")
img = cv2.imread("image.jpg")
img = cv2.resize(img,(400,300))
cv2.imshow("Output Window", img)
cv2.waitKey(0)

#Importing and playing a video

cap = cv2.VideoCapture("video.mp4")

while True:
    success, img = cap.read()
    cv2.imshow("Video window",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

#Using Webcam for video

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

#setting the Exposure for webcam
cap.set(10,100)

while True:
    success, img = cap.read()
    cv2.imshow("Video window",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break