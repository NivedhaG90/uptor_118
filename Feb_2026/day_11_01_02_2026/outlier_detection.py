import pandas as pd

#Quantile is a method in dataframe pandas which means quantity.

data = {
    "price": [200,220,250,270,300,320,350,1000]
}

df = pd.DataFrame(data)

Q1 = df["price"].quantile(0.25)
Q3 = df["price"].quantile(0.75)

IQR = Q3 - Q1
#InterQuaritile Range  - margin of changes between 0.25 and 0.75
print(Q1,Q3,IQR)

#two extinct data (lower and upper) without any relation - outlier
# to find range, always use 1.5

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print(lower_bound, upper_bound)

#anything that comes below lower_bound and anything that comes above upper_bound are considered as outliers

#as per data, 1000 will be outlier

outliers = df[(df["price"] < lower_bound) | (df["price"] > upper_bound)]
print(outliers)

import matplotlib.pyplot as plt

plt.boxplot(df['price'])
plt.ylabel("Price")
plt.title('Box plot using IQR method')
plt.show()

#This is specific to each column and is used to outlier outlier data from dataset. If we have outlier, our module accuracy will be affected. So we will remove it after identifying.
