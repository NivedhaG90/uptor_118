import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("diamonds.csv")
print(df.isna().sum().sum())


label_encoding_object = LabelEncoder()
df['cut'] = label_encoding_object.fit_transform(df['cut'])

print(df['cut'][1])
print(df['cut'][2])

print(df.isna().sum().sum())

#Returns diff null count before and after applying LabelEncoder

#every column we choose to be numeric in data science

# print("Cut category -> Number Mapping")
# for i,category in enumerate(label_encoding_object.classes_):
#     print(f" '{category}' -> {i}")