# import matplotlib.pyplot as plt
# import numpy as np
#
# #barplot - number vs category
#
# # Generate data for a bar plot
# categories = ['Maths', "Science", "English"]
# values = [96, 85, 73]
#
# #Create a Bar plot
# plt.bar(categories, values, label="Bar Chart", color="orange", edgecolor="black")
#
# #add labels and title
# plt.xlabel("Categories")
# plt.ylabel("Values")
# plt.title('Scatter plot: Categories Comparison')
#
# plt.legend()
#
# plt.show()

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("D:/PycharmProjects/Uptor_118/jan_2026/day_5_11_01_2026/diamonds.csv")

# try:
#     #Create a Bar plot
#     plt.bar(df["cut"], round(df["price"]), label="Bar Chart", color="yellow", edgecolor="black")
#
#     #add labels and title
#     plt.xlabel("X Data")
#     plt.ylabel("Y Data")
#
#     plt.legend()
#
#     plt.show()
# except Exception as ex:
#     print(ex)

sum_price = df.groupby("cut")["price"].sum()
plt.bar(sum_price.index, sum_price.values)
plt.xlabel("X Data")
plt.ylabel("Y Data")
plt.show()

#if u notice graph, it shows exponential value (1e7)

