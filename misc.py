import cv2
import numpy as np 

img=cv2.imread('messi.jpg',cv2.IMREAD_COLOR)
img[100,100]=(120,200,45)
print(img[100,100])