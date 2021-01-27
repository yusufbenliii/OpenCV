import cv2
import numpy as np
from stackImages import stackImages
# Contours / Shape Detection
def getContours(img):
    contours, hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        cv2.drawContours(imgContour,cnt,-1,(255,0,0),3)
        print(area)
path = r"Resources/shapes2.jpg"

img = cv2.imread(path)
img = cv2.resize(img,(460,460))
imgContour = img.copy()
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(img,(7,7),1)
imgCanny = cv2.Canny(imgBlur,50,50)
imgBlank = np.zeros_like(img)


imgStack = stackImages(0.4,([img,imgGray,imgBlur], [imgCanny,imgContour,imgBlank]))

cv2.imshow("Stack", imgStack)


cv2.waitKey(0)
