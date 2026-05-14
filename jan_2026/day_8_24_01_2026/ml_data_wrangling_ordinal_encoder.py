import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

df = pd.read_csv("diamonds.csv")
print(df.isna().sum().sum())


label_encoding_object = OrdinalEncoder()
df['cut'] = label_encoding_object.fit_transform(df[['cut']])

print(df['cut'][1])
print(df['cut'][2])

print(df.isna().sum().sum())

#Returns same null count before and after applying OrdinalEncoder