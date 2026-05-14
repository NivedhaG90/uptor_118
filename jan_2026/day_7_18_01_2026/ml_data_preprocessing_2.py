import pandas as pd

# in pandas only integer, float or object.

#df - dataframe
df = pd.read_csv(r"D:\PycharmProjects\Uptor_118\jan_2026\day_5_11_01_2026\diamonds.csv")
# print(df)
#
# column_data_types = df.dtypes
# print(column_data_types)
#
# column_data_types = df['cut'].dtype
# print(column_data_types)
#
# column_data_types = df[['cut', 'carat']].dtypes
# print(column_data_types)

#This is to show the actual dimension of the input
# checking_dimensions = df.ndim
# print(checking_dimensions)

#print(df['cut']) #syntax for reading only one column

#print(df[['cut', 'carat']]) #Syntax for reading more than one column

# O - Object

# columns = df.columns
# for x in columns:
#     if df[x].dtype == 'O':
#         print(x)

# categorical_columns = []
# numerical_columns = []
#
# column_data = df.columns
# for x in column_data:
#     if df[x].dtype == 'O': #or u can use if df[x].dtype == object
#         categorical_columns.append(x)
#     else:
#         numerical_columns.append(x)
#
# print(categorical_columns)
# print('--------------------')
# print(numerical_columns)

# columns = df.columns
# for x in columns:
#     if df[x].dtype != 'O':
#         print(x)
#
# columns = df.columns
# for x in columns:
#     if df[x].dtype not in [object]:
#         print(x)

# category_detailing = df['cut'].value_counts() #total values of each category
# print(category_detailing)

# category_detailing = df['cut'].unique() #unique or discrete category name
# print(category_detailing)
#
# category_detailing = df['cut'].nunique() #total unique category count
# print(category_detailing)

# finding_null_value = df.isna() #to check if it has null data or not
# print(finding_null_value)

finding_null_value = df.isna().sum() #to check null count on each column base
print(finding_null_value)

finding_null_value = df.isna().sum().sum() #to list total null count across df
print(finding_null_value)
