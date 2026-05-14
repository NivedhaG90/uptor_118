from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import pandas as pd

df = pd.read_csv("house_price_bd.csv")
df.dropna(inplace=True)

df['Price_in_taka'] = df['Price_in_taka'].replace({"৳":"",",":""},regex=True).astype(int)

print(df['Price_in_taka'])
print(df['Price_in_taka'].dtype)

print(df['Floor_no'].dtype)
print(df['Floor_no'].unique())

x = df[['Bedrooms', 'Bathrooms']]
y = df['Price_in_taka']

x_train, x_test, y_train, y_test = train_test_split(x, y ,train_size=0.7, random_state=42)

model = LinearRegression()
model.fit(x_train, y_train)

prediction = model.predict(x_test)
print(prediction)

accuracy_testing = r2_score(y_test, prediction)
print(accuracy_testing)