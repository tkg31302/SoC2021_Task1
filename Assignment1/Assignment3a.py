import cv2

img = cv2.imread("Resources/Photo.jpg")
res = cv2.resize(img, (640,720))

img_gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)

img_invert = cv2.bitwise_not(img_gray)

img_smoothing = cv2.GaussianBlur(img_invert, (21, 21), 0)

def dodgeV2(x, y):
    return cv2.divide(x, 255 - y, scale=256)

final_img = dodgeV2(img_gray, img_smoothing)


cv2.imshow("Image", res)
cv2.imshow("Sketch", final_img)
cv2.waitKey(0)
