import cv2
import numpy as np


img= cv2.imread("Resources/assignment2.png")
res = cv2.resize(img, (300, 300))
imgGray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
rows, cols = imgGray.shape

M = np.float32([[1, 0, rows/10], [0, 1, cols/10]])
translation = cv2.warpAffine(res, M, (cols, rows))

M1 = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 1)
rotation = cv2.warpAffine(res, M1, (cols, rows))

for i in range(4):
	cv2.imshow("translate " + str(i+1), translation)
	cv2.imshow("rotate " + str(i+1), rotation)
	translation = cv2.warpAffine(translation, M, (cols, rows))
	rotation = cv2.rotate(rotation, cv2.ROTATE_90_CLOCKWISE)

pts1 = np.float32([[50,50], [200,50], [50,200]])
pts2 = np.float32([[10,100], [200,50], [100,250]])
M2 = cv2.getAffineTransform(pts1, pts2)
AffineTransform = cv2.warpAffine(res, M2, (cols, rows))
cv2.imshow("Affine Transformated", AffineTransform)

kernel = np.ones((5,5), np.float32)/25
convolute2D = cv2.filter2D(res, -1, kernel)
cv2.imshow("2D Convoluted", convolute2D)

blur = cv2.blur(res, (5,5))
cv2.imshow("Blur", blur)
G_Blur = cv2.GaussianBlur(res, (11,11), 0)
cv2.imshow("gblur", G_Blur)
median = cv2.medianBlur(res, 5)
cv2.imshow("Median Blur", median)
blur1 = cv2.bilateralFilter(res, 9, 75, 75)
cv2.imshow("Bilateral Filtering", blur1)

cv2.waitKey(0)
cv2.destroyAllWindows()