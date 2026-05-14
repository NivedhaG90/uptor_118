import matplotlib.pyplot as plt
import numpy as np

data = [np.random.normal(0,1,100), np.random.normal(0,1.5,100), np.random.normal(0,2,100)]
plt.boxplot(data, tick_labels=['Group1', 'Group2', 'Group3'], patch_artist=True, notch=True)

#finding un necessary values in a data is boxplot
#box plot is a plot which needed only one axis

# data = np.random.normal(0,1,100)
# print(data)
# plt.boxplot(data, patch_artist=True, notch=True)

plt.xlabel("Groups")
plt.ylabel("Values")
plt.title('Box plot: Group Comparison')

#In output u will notice some o at one side sometimes - outlayer. If top +, down -.

plt.show()