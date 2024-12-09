import cv2

img = cv2.imread('messi.jpg',1)
#img = cv2.resize(img, (0,0), fx=.5, fy=.5)
print(img.shape)
tag = img[0:100,60:300]
img[40:140,200:440] = tag
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
