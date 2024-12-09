import cv2
import numpy as np 

img=cv2.imread('messi.jpg',cv2.IMREAD_COLOR)
h,w=img.shape[:2]
s_points=np.float32([[0,0],[w-1,0],[0,h-1]])
d_points=np.float32([[150,0],[w-1+150,0],[0,h-1]])
mat = cv2.getAffineTransform(s_points, d_points)

img2=cv2.warpAffine(img, mat, (w+150,h))

cv2.imshow("original",img)
cv2.imshow('trans',img2)
cv2.waitKey()
#cv2.destroyAllWindows()