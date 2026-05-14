import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,4,6,8,6]

# plt.plot(x,y)
# plt.show()

#u can use o,x for marker
plt.plot(x,y, marker="*", color="blue")
plt.xlabel("X Data")
plt.ylabel("Y Data")
plt.show()