import numpy as np
import matplotlib.pyplot as points

x = np.array(["Panthers", "Ravens", "Shooting Stars", "Rockets"])
y =np.array([6,4,9,8])

points.title("Points scored by teams")
points.xlabel("Team name")
points.ylabel("Number of points")

points.bar(x,y, color="yellow")
#points.grid(axis="y")
points.show()
