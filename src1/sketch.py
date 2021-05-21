import numpy as np
import cv2
img=cv2.imread("a.jpg")
img=cv2.resize(img,(800,700))
def nothing(x):
    pass
cv2.namedWindow("Color Adjustment",cv2.WINDOW_NORMAL)
cv2.resizeWindow("Color Adjustment",(300,300))
cv2.createTrackbar("Scale","Color Adjustment",0,255,nothing)
cv2.createTrackbar("Color","Color Adjustment",0,255,nothing)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
while True:
    scale=cv2.getTrackbarPos("Scale","Color Adjustment")
    clr=cv2.getTrackbarPos("Color","Color Adjustment")
    inverted_gray = clr - gray
    blur_img=cv2.GaussianBlur(inverted_gray,(21,21),0)
    inverted_blur=clr-blur_img
    fltr=cv2.divide(gray,inverted_blur,scale=scale)
    cv2.imshow("opt",fltr)
    k=cv2.waitKey(0)
    if k== ord("q"):
        break
    if k==ord("s"):
        cv2.imwrite("res.jpg",fltr)
cv2.destroyAllWindows()