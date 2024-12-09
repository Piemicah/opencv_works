import cv2 as cv 
import numpy as np

img = cv.imread('messi.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cannied = cv.Canny(img, 50, 240)
cv.imshow('winname', cannied)

cv.waitKey()
cv.destroyAllWindows()