import cv2
import matplotlib.pyplot as plt

img=cv2.imread('messi.jpg',cv2.IMREAD_UNCHANGED)

h,w=img.shape[:2]

sf=50
x=int(sf*w/100)
y=int(sf*h/100)
ds=(x,y)

output=cv2.resize(img, ds)

cv2.imshow("original", img)
cv2.imshow("res", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(h)