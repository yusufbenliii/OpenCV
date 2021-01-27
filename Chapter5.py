import cv2
import numpy as np
# Warp Perspective

img = cv2.imread(r"Resources/cards.png")
width,height = 250, 350
pts1 = np.float32([[116,229],[303,197],[160,504],[372,457]])  # corners of the image which we want to transform on the real image
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])  # corners of the output image
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow("Image",img)
cv2.imshow("Output",imgOutput)

cv2.waitKey(0)
