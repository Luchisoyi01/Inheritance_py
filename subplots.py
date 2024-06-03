import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1) #the subplot has 1 row, 2 column and it is the 1st plot
plt.plot(x,y)
plt.title("SALES") #Shows the title of the first subplot

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2) #the subplot has 1 row, 2 column and it is the 2nd plot
plt.plot(x,y)
plt.title("INCOME")  #Shows the title of the second subplot

plt.suptitle("MY SHOP") #it shows the title of the entire figure
plt.show()