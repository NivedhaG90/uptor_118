import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler

df = pd.read_csv("D:/PycharmProjects/Uptor_118/jan_2026/day_8_24_01_2026/diamonds.csv")
print(df)

std_scaler_obj = StandardScaler()
df['price'] = std_scaler_obj.fit_transform(df[['price']])
print(df)

std_scaler_obj = MinMaxScaler()
df['price'] = std_scaler_obj.fit_transform(df[['price']])
print(df)