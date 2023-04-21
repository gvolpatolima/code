import numpy as np
import matplotlib.pyplot as plt


x,y = np.meshgrid(np.linspace(-5,5,20),np.linspace(-5,5,20))

u = 3
v = -1
deg = np.arctan(y ** 3 - 3 * y - x)
widths = np.linspace(0, 2, x.size)

plt.quiver(x, y, np.cos(deg), np.sin(deg), linewidths=widths)
plt.show()
