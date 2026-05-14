from sklearn.linear_model import LinearRegression
import pandas as pd
from sklearn.model_selection import train_test_split

year = [2000,2001,2002,2003,2004,2005]
price = [10000,20000,30000,40000,50000,60000]

df = pd.DataFrame({"purchase_year":year, "Housing_price" : price})
print(df)

x = df[["purchase_year"]] #doublesquare - bcz this is the data we are going to give to model as input to learn and we give in 2 dimension
y = df["Housing_price"] #target is one column only. so we give in single dimension.

x_train, x_test, y_train, y_test = train_test_split(x,y, train_size=0.7, random_state=42)
#train_size=0.7 -> denotes 70% of the data to be used for training
#random_state=42 -> denotes it should always return the same output when I run any number of times. It can be any number not necessarily 42

print(x_train)

linear_model = LinearRegression()
linear_model.fit(x_train,y_train)

prediction = linear_model.predict(x_test) #anything other than x_train will be printed under x_test
print(prediction)

