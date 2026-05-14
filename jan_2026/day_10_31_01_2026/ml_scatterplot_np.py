import matplotlib.pyplot as plt
import numpy as np

# Generate data for a scatter plot
x = np.random.rand(100)
y = 2 * x + np.random.randn(100)

#Create a Scatter plot
plt.scatter(x, y, label="Random Data", color="green", marker="o")

#add labels and title
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title('Scatter plot: Random data')

plt.legend()

plt.show()