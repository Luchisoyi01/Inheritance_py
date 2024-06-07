import numpy
import matplotlib.pyplot as plt

x = numpy.random.uniform(0.0, 10.0, 100)

plt.hist(x, 5)
plt.show()