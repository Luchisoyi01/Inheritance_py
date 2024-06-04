import numpy as np
import matplotlib.pyplot as pie

y= np.array([203, 103, 101, 73, 60])
mylabels= ["Apple", "Banana", "Grapefruit", "Raspberry", "orange"]

font1 = {
  "family":"times new roman",
  "fontweight":"bold",
  "size": 20
}

pie.title("Fruit distribution in Meru", fontdict = font1 , loc="left")
pie.pie(y, labels = mylabels)
pie.legend(title = "Fruits in Meru:")
pie.show()
