import cv2
import numpy as np 

img=cv2.imread('messi.jpg',cv2.IMREAD_COLOR)
h,w=img.shape[:2]

kernel=np.ones((5,5),np.float32)/25.0

img2=cv2.filter2D(img,-1,kernel)

cv2.imshow("original",img)
cv2.imshow('blured',img2)
cv2.waitKey()
cv2.destroyAllWindows()