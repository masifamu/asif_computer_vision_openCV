import cv2
print("Package Imported")
image = cv2.imread("resources/lena.png")
cv2.imshow("Lena image", image)
cv2.waitKey(0)