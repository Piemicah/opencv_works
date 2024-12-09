import cv2 as cv 
import numpy as np

h,w=600,600
r=200
red = np.zeros((h,w,3))
green = np.zeros((h,w,3))
blue = np.zeros((h,w,3))

cv.circle(red,(r,h-r),r,(0,0,1),-1)
cv.circle(blue,(w-r,h-r),r,(1,0,0),-1)
cv.circle(green,(w//2,r),r,(0,1,0),-1)

img1 = cv.add(red,green)
img = cv.add(img1,blue)

cv.imshow("ghhg", img)
cv.waitKey()