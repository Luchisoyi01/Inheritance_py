import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 3, 5, 7])
ypoints = np.array([2, 10, 2, 9])

plt.plot(xpoints, ypoints)
plt.show()


#If we do not specify the points on the x-axis, they will get the default values 0, 1, 2, 3 etc., depending on the length of the y-points.