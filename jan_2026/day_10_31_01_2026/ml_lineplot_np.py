import matplotlib.pyplot as plt
import numpy as np

# Generate data for a line plot
x = np.linspace(0, 10, 100)
#print(x) #It will come in an increasing order
y = np.sin(x)

#Create a line plot
plt.plot(x, y, label="Sine wave", color="blue", linestyle="-", linewidth=2)

#add labels and title
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title('Line plot: Sine wave')

plt.legend()

plt.show()