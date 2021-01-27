import cv2
# Read Images Videos and Webcams

img = cv2.imread(r"Resources/lena.png")
cv2.imshow("OUTPUT", img)
cv2.waitKey(0)

cap = cv2.VideoCapture(0) # for video (videoPath) r"Resources/testVideo.mp4"

cap.set(3, 480)  # 3 is height
cap.set(4, 620)  # 4 is weight
cap.set(10, 100)  # 10 is brightness
while True:
    success, img = cap.read()
    cv2.imshow("Video", img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

