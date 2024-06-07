import numpy
import matplotlib.pyplot as plt

x = numpy.random.normal(10.0, 1.0, 1000000)
#y = numpy.random.uniform(10.0, 1.0, 1000000)
plt.hist(x, 100)
#plt.hist(y, 100)
plt.show()

'''
A normal distribution graph is also known as the bell curve 
because of it's characteristic shape of a bell.
'''