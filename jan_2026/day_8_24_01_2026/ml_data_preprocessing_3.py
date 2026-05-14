import pandas as pd
from sklearn.impute import SimpleImputer

df = pd.read_csv("diamonds.csv")
print(df.isna().sum().sum())

simple_imputing_object = SimpleImputer(strategy="most_frequent") #it fills the values with mean
df['y'] = simple_imputing_object.fit_transform(df[['y']]) #this can be applied only for numerical colum

print(df['y'][14])
print(df['y'][29])

#{'constant', 'median', 'most_frequent', 'mean' }
simple_imputing_object = SimpleImputer(strategy="constant", fill_value=90)
df['y'] = simple_imputing_object.fit_transform(df[['y']]) #this can be applied only for numerical columns

#yu cannot use two strategy for same column

print(df['y'][14])
print(df['y'][29])

print(df.isna().sum().sum())