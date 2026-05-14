import pandas as pd

file_content = pd.read_csv(r"D:\PycharmProjects\Uptor_118\jan_2026\day_5_11_01_2026\diamonds.csv")

""" Concept of reading rows with : is called slicing. : is range specifier. u should specify startindex:endindex"""
# reading_specific_row = file_content[0:25]
# print(reading_specific_row)
#
# reading_specific_row = file_content[53938:]
# print(reading_specific_row)
#
# reading_specific_row = file_content[:] #start index till last index
# print(reading_specific_row)

""" Below concept is reading of both rows and columns.
loc - location identifier
"""

# reading_specific_row = file_content.loc[0:25, ["cut"]] #start index till last index
# print(reading_specific_row)
#
# reading_specific_row = file_content.loc[0:25, ["cut", "color"]] #start index till last index
# print(reading_specific_row)
#
# reading_specific_row = file_content.iloc[0:25, 1:3] #start index till last index
# print(reading_specific_row)

# Any data other than int and float are considered as object
file_information = file_content.info()
print(file_information)

#describe function to understand numerical or stats related numbers
file_description = file_content.describe()
print(file_description)