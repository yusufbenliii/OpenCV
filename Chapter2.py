import cv2
import numpy as np
# Basic Functions

img = cv2.imread(r"Resources/lena.png")
#cv2.imshow("Image", img)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#cv2.imshow("Gray Image", imgGray)

imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
#cv2.imshow("Blur Image", imgBlur)

imgCanny = cv2.Canny(img, 150, 200)  # second and third parameters are threshold values
cv2.imshow("Canny Image", imgCanny)

kernel = np.ones((5,5),np.uint8)

imgDilation = cv2.dilate(imgCanny,kernel,iterations=1)  # to increase thickness of edges
cv2.imshow("Dilation Image",imgDilation)

imgEroded = cv2.erode(imgDilation,kernel,iterations=1)  # opposite of dilation
cv2.imshow("Eroded Image",imgEroded)

cv2.waitKey(0)
