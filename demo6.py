import matplotlib.pyplot as plt
import numpy as np
from numpy import random

img = np.zeros([400, 400,3])

def paint(n):
    for i in range(int(400/n)):
        img[i*n:n*(i+1),i*n:n*(i+1)] = (random.rand(),random.rand(),random.rand())

paint(100)
im = plt.imshow(img)
plt.show()