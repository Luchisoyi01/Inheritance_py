import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 3, 5, 7])
ypoints = np.array([2, 10, 2, 9])

plt.plot(xpoints, ypoints)
plt.show()


#if the x axis points are not defined it follows 0,1,2,3,4 ....etc