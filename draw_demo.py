import cv2
import numpy as np

h,w=(600,600)
img=np.ones((h,w,3))
cv2.line(img,(0,0),(w-1,h-1),(0,0,0),3)
cv2.line(img,(w-1,0),(0,h-1),(1,0,0),3)
cv2.circle(img,(int(w/2),int(h/2)),int(w/2),(1,0,1),3)
cv2.ellipse(img,(int(w/2),int(h/2)),(200,150),0,0,360,(0,0,1),3)
cv2.imshow('draw',img)
cv2.waitKey()
cv2.destroyAllWindows()