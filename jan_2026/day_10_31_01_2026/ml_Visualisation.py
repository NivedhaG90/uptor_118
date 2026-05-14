import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,4,6,8,6]

# plt.plot(x,y)
# plt.show()

#u can use o,x for marker. scatter means no connectivity. It will just be there. Plot and scatter will have both x and y as number.
# c = x means it will take diff colour for each quantity. here - 5
# In python, under visualisation there is a concept called cmap - colour map. They have a group for a set of colours.
#plt.scatter(x,y, marker="*", c=x)
plt.scatter(x,y, marker="o", c = x, cmap="magma", label="scatter plot")
plt.xlabel("X Data")
plt.ylabel("Y Data")
plt.colorbar() #It displays the family of colors from which its derived
plt.legend()
plt.show()