import cv2
import numpy as np 

img=cv2.imread('messi.jpg',cv2.IMREAD_COLOR)

trans_matrix=np.float32([[1,0,50],[0,1,50]])

h,w=img.shape[:2]

img2=cv2.warpAffine(img, trans_matrix, (w+50,h+50))

cv2.imshow("original",img)
cv2.imshow('trans',img2)
cv2.waitKey()
#cv2.destroyAllWindows()