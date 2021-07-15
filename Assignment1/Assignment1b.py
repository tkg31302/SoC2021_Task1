import cv2

img = cv2.VideoCapture(0)

img.set(3, 640)
img.set(4, 480)

while True:
    success, img1=img.read()
    imgGray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Gray Img", imgGray)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
