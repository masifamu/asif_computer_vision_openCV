import cv2
print("Lets Capture a vidio using webcam")
cap = cv2.VideoCapture(0)   # 0 for default camera (laptop camera)
                            # if we have multiple cams use the corresponding ID here.
cap.set(3, 640) # ID:3 is for width
cap.set(4, 480) # ID:4 is for Height
cap.set(10, 100) # ID:10 is for brightness

while True:
    success, img = cap.read()
    cv2.imshow("video", img)
    if cv2.waitKey(33) & 0xFF == ord('q'):
        break

# so waitkey(arg) generateds delay in milliseconds
# it returns the ASCII value of the pressed key at which the loop breaks.
# we are taking only 8bits (0xFF) and compare if the pressed key is 'q'