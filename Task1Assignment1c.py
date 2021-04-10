import cv2
import numpy as np

img = cv2.imread("Resources/rose.jpg")
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
hsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)

lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])

mask = cv2.inRange(hsv, lower_blue, upper_blue)

res = cv2.bitwise_and(img1,img1, mask= mask)


cv2.imshow('frame',img)
cv2.imshow('mask',mask)
cv2.imshow('res',res)

cv2.waitKey(0)