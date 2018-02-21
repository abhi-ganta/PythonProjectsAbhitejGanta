from matplotlib import pyplot
import random

x_values = [0, 4, 7, 20, 22, 25]
y_values = [0, 2, 4, 8, 16, 32]
pyplot.plot(x_values, y_values, "b-")

x2_values = []
y2_values = []

for n in range(15):
    y2_values.append(random.randint(0, 20))
    x2_values.append(random.randint(0, 20))

pyplot.plot(x2_values, y2_values, "ro")


pyplot.ylabel("Value")
pyplot.xlabel("Time")
pyplot.title("Test plot")

pyplot.show()
