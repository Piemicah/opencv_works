import cv2
import numpy as np

img=cv2.imread('messi.jpg')

roi = img[:100,:100]

red=np.ones(roi.shape,dtype=roi.dtype)

red[:]=[0,0,255]

mask = np.zeros(roi.shape[:2],dtype=np.uint8)

mask_inv=cv2.bitwise_not(mask)

black = cv2.bitwise_and(roi,roi,mask=mask)
white = cv2.bitwise_and(roi,roi,mask=mask_inv)

combo = cv2.add(red,black)

img[:100,:100]=combo

cv2.imshow('mask',img)
cv2.waitKey()
cv2.destroyAllWindows()