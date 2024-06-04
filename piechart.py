import numpy as np
import matplotlib.pyplot as pie

y= np.array([203, 103, 101, 73, 60])
mylabels= ["Apple", "Banana", "Grapefruit", "Raspberry", "orange"]


pie.pie(y, labels = mylabels)
pie.legend()
pie.show()
