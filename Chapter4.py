import cv2
import numpy as np
# Shapes and Texts

#img = np.zeros((512, 512)) Grayscale Image not RGB (Blakc)
#img = np.ones((512, 512)) white

img = np.zeros((512, 512, 3), np.uint8)
#img[:] = 255, 255, 255  # Convert color of image

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)  # image,starting coor, ending coor, color, thickness
'''Here we set ending coordinate by image shape. First we wrote width and then height'''
cv2.rectangle(img,(0,0),(250,350),(0,0,255),cv2.FILLED)  # instead of thickness we used cv2.Filled
cv2.circle(img,(400,50),30,(255,255,0),5)
cv2.putText(img,"OpenCV",(350,150),cv2.FONT_HERSHEY_SIMPLEX,1,(0,150,0),1)  # image, text, coordinates, font, size, color, thickness


cv2.imshow("Image",img)
cv2.waitKey(0)
