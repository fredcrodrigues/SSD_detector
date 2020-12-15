import cv2
import numpy as np


img = cv2.imread("70_1_2_20170110181645374.jpg")
img = cv2.resize(img , (300 , 300) , interpolation=cv2.INTER_CUBIC )
img = cv2.blur(img ,(3,3))
cv2.imshow("image_train" , img)

cv2.waitKey(0)


