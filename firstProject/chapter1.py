import cv2
print("Reading a video and displaying it")
cap = cv2.VideoCapture("resources/1680871817378.mp4")

while True:
    success, img = cap.read()
    cv2.imshow("video", img)
    if cv2.waitKey(33) & 0xFF == ord('q'):
        break

# so waitkey(arg) generateds delay in milliseconds
# it returns the ASCII value of the pressed key at which the loop breaks.
# we are taking only 8bits (0xFF) and compare if the pressed key is 'q'