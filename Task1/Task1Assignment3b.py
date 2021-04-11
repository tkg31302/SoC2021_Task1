import cv2

img = cv2.VideoCapture(0)

img.set(3, 1000)
img.set(4, 1000)

while True:
    success, img1=img.read()
    imgGray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img_invert = cv2.bitwise_not(imgGray)
    img_smoothing = cv2.GaussianBlur(img_invert, (21, 21), sigmaX=0, sigmaY=0)
    def dodgeV2(x, y):

        return cv2.divide(x, 255 - y, scale=256)


    final_img = dodgeV2(imgGray, img_smoothing)
    cv2.imshow("Sketch", final_img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break