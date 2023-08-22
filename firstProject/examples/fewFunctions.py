import cv2
import numpy as np

img = cv2.imread("resources/lena.png")
kernal = np.ones((5,5),np.uint8)
# cvtColor() is used to convert img to any color space
imgGrey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGrey,(7,7),0)
imgCanny = cv2.Canny(img,100,100) # edge detection
imgDialation = cv2.dilate(imgCanny, kernal,iterations=1) # how many iterations we need to apply kernal on the imgCanny
                                                        # this is only for edge enhancement, more iteration more thickness
imgEroded = cv2.erode(imgDialation,kernal,iterations=1) # reverse of dialation

cv2.imshow("GreyImage", imgGrey)
cv2.imshow("BlurImage", imgBlur)
cv2.imshow("CannyImage", imgCanny)
cv2.imshow("DialationImage", imgDialation)
cv2.imshow("ErodedImage", imgEroded)

cv2.waitKey(0)