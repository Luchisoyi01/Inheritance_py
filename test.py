import numpy
import matplotlib.pyplot as test
numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

test_x = x[80:]
test_y = y[80:]
test.scatter(test_x, test_y)
test.show()