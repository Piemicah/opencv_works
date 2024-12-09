import matplotlib.pyplot as plt
import numpy as np
from numpy import random

img = np.zeros([400, 400,3])

# this function generates m x m color squares
def paint(m):
    n = int(400/m)
    for i in range(m):
        for j in range(m):
            img[n*i:n*(i+1),n*j:n*(j+1)] = (random.rand(),random.rand(),random.rand())
    return img

fig, ax = plt.subplots(1, 2)
im = paint(4)
ax[0].imshow(im)

im2 = paint(5)
ax[1].imshow(im2)
plt.show()