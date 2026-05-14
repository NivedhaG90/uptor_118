from sklearn.linear_model import LinearRegression
import pandas as pd

year = [2000,2001,2002,2003,2004,2005]
price = [10000,20000,30000,40000,50000,60000]

df = pd.DataFrame({"purchase_year":year, "Housing_price" : price})
print(df)

x = df[["purchase_year"]] #doublesquare - bcz this is the data we are going to give to model as input to learn and we give in 2 dimension
y = df["Housing_price"] #target is one column only. so we give in single dimension.

linear_model = LinearRegression()
linear_model.fit(x,y)

year_to_find = [2006, 2007]
df_target = pd.DataFrame({"purchase_year":year_to_find})

print("---------------------------")

prediction = linear_model.predict(df_target)
print(prediction)

df_target["Housing_price"] = prediction

final_df = pd.concat([df, df_target], axis=0) #This appends the prediction with 0 and 1 index
print(final_df)

final_df = pd.concat([df, df_target], axis=0, ignore_index=True) #This shows the prediction with earlier index continuation
print(final_df)

#axis = 0 is default. you can even not required to give it. If u want to add a new column, u should give axis=1

#training and testing - if u have 100 data, give 70 data for training and remaining 30 data test and see if the prediction is correct.

