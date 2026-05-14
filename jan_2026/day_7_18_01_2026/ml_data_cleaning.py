import pandas as pd

df = pd.read_csv(r"D:\PycharmProjects\Uptor_118\jan_2026\day_5_11_01_2026\diamonds.csv")
# print(df)

# print("before dropping")
# finding_null_data = df['cut'].isna().sum()
# print(finding_null_data)

""" Below code is to remove the null data """
#df['cut'] = df['cut'].dropna(inplace = True) #not working
# df.dropna(subset=['cut'], inplace=True)
#
# print("after dropping")
# finding_null_data = df['cut'].isna().sum()
# print(finding_null_data)

# #to remove all the null values
# finding_null_data = df.isna().sum()
# print(finding_null_data)
# df.dropna(inplace=True)
# finding_null_data = df.isna().sum()
# print(finding_null_data)
#
# df.to_csv("diamonds_null_removed.csv") # To write the data to a new csv file after removing null data

#Nan - not available number
""" Below code is to fill the null data"""
df['cut'] = df['cut'].fillna(1000)
df.to_csv("diamonds_fill_null.csv")

#Sensible filling
df['carat'] = df['carat'].fillna(df['carat'].mean())