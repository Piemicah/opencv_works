import cv2
import numpy as np

h,w=300,300
img1=np.zeros((h,w,3),np.uint8)
img2=np.zeros((h,w,3),np.uint8)
img1[:]=[0,200,0]
img2[:]=[0,200,255]

#imgadd=cv2.add(img1,img2)
imgadd=cv2.subtract(img1, img2)
#imgadd=img2-img1
cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.imshow('imgadd',imgadd)
cv2.waitKey()
cv2.destroyAllWindows()