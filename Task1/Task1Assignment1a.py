import cv2
import numpy as np

img = cv2.imread("Resources/Photo.jpg")
res = cv2.resize(img, (640,720))

imgGray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)

thresh, img1 = cv2.threshold(imgGray, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("Gray Img", img1)

img2 = cv2.adaptiveThreshold(imgGray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 7, 2)
cv2.imshow("AGray Img", img2)

cv2.waitKey(0)

