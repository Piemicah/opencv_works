import cv2 as cv 
import numpy as np

img = cv.imread('chioma.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

faces = face_cascade.detectMultiScale(gray)

for (x,y,w,h) in faces:
    cv.rectangle(img, (x,y), (x+w,y+h), (255,0,0),2)

cv.imshow('winname', img)

cv.waitKey()
cv.destroyAllWindows()