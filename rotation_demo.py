import cv2
import numpy as np 

img=cv2.imread('messi.jpg',cv2.IMREAD_COLOR)
h,w=img.shape[:2]
rot_matrix=cv2.getRotationMatrix2D((w/2,h/2), 45, 1)


img2=cv2.warpAffine(img, rot_matrix, (w,h))

cv2.imshow("original",img)
cv2.imshow('trans',img2)
cv2.waitKey()
cv2.destroyAllWindows()