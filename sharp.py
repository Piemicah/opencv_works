import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('messi.jpg')

k1 = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
k2 = np.array([[1,1,1],[1,-7,1],[1,1,1]])
k3 = np.array([[2,2,2],[1,-7,1],[2,2,2]])/7
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

sharp1=cv.filter2D(img, -1, k1)
sharp2=cv.filter2D(img, -1, k2)
sharp3=cv.filter2D(img, -1, k3)

sharp=[img,sharp1,sharp2,sharp3]
l=len(sharp)
for i in range(l):
    cv.imshow(str(i),sharp[i])
   

# cv.imshow('original',img)
# cv.imshow('k1', sharp1)
# cv.imshow('k2', sharp2)
# cv.imshow('k3', sharp3)

cv.waitKey()
cv.destroyAllWindows()