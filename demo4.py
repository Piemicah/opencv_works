import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,6*np.pi,200)
y1 = np.sin(x)
y2 = np.cos(x)

fig, ax = plt.subplots(1,2)
ax[0].plot(x, y1,'g--')
ax[0].set_title('sin')
ax[1].plot(x, y2)
ax[1].set_title('cos')
plt.show()
