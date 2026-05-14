import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("D:/PycharmProjects/Uptor_118/jan_2026/day_5_11_01_2026/diamonds.csv")


plt.scatter(df['x'],df['price'], marker="o", c = df['x'], cmap="magma", label="scatter plot")
plt.xlabel("X Data")
plt.ylabel("Y Data")
plt.colorbar() #It displays the family of colors from which its derived
plt.legend()
plt.show()