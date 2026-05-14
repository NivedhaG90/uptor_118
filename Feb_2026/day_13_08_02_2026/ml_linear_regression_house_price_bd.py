from sklearn.linear_model import LinearRegression
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

#tested by me

file_content = pd.read_csv(r"house_price_bd.csv")
file_content.dropna(inplace=True) #missed this line alone earlier

#If u are unsure which column to pick for linear expression, there is an inbuilt function which will suggest

file_content['Price_in_taka'] = file_content['Price_in_taka'].replace({"৳":"",",":""},regex=True).astype(int)

print(file_content)

df = pd.DataFrame({"floor_area":file_content['Floor_area'], "price" :file_content['Price_in_taka']})
print(df)

x = df[["floor_area"]]
y = df["price"]

x_train, x_test, y_train, y_test = train_test_split(x,y, train_size=0.7, random_state=42)

print(x_train)

linear_model = LinearRegression()
linear_model.fit(x_train,y_train)

prediction = linear_model.predict(x_test) #anything other than x_train will be printed under x_test
print(prediction)

metric_evaluation = r2_score(y_test, prediction)
print(metric_evaluation)