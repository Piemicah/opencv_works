import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import cv2

fig, ax = plt.subplots(1, 3)
img = plt.imread('messi.jpg')
img2 = 1 - img
img3=img.copy()
img3[img<160]=0
img3[img>=160]=255
ax[0].imshow(img)
ax[1].imshow(img2)
ax[2].imshow(img3)
#cv2.imwrite('mmm2.jpg',img2)
plt.show()
print(img.shape)
print(img)
#s=open('xx.txt','wb') write binary
#np.save(s,img)
# s=open('xx.txt','rb')
# m=np.load(s)
# print(m)
# plt.imshow(m)
# plt.show()