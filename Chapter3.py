import cv2
import numpy as np

# OpenCV Convention

img = cv2.imread(r"Resources/chess.jpg")
cv2.imshow("Image", img)
print(img.shape)  # 500 500 3 , width height RGB

imgResize = cv2.resize(img,(300,200))
cv2.imshow("Image Resized", imgResize)
print(imgResize.shape)  # 200 300 3 , width height RGB

imgCropped = img[0:200,200:500]  # height 0 to 200, width 200 to 500
cv2.imshow("Image Cropped", imgCropped)

cv2.waitKey(0)
