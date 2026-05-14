import pandas as pd

# try:
#     #file_reading = pd.read_csv("D:/PycharmProjects/Uptor_118/jan_2026/day_5_11_01_2026/diamonds.csv")
#     #sometimes \u will be inbuilt standards or functions. hence we may get unicode error. Its better to use r before. r - raw data
#     file_reading = pd.read_csv(r"D:\PycharmProjects\Uptor_118\jan_2026\day_5_11_01_2026\diamonds.csv")
#     print(file_reading)
# except Exception as ex:
#     print(ex)
#
# try:
#     file_reading = pd.read_csv(r"D:\PycharmProjects\Uptor_118\jan_2026\day_5_11_01_2026\diamonds.csv")
#     print(file_reading)
# except Exception as ex:
#     print(ex)

""" User defined function for file reading of CSV format"""
def csv_file_reading(file_path): #function definition
    file_content = pd.read_csv(file_path) #function operation
    return file_content #function output

def csv_column_reader(file):
    column_names = file.columns
    return column_names

recieved_file_content = csv_file_reading(r"D:\PycharmProjects\Uptor_118\jan_2026\day_5_11_01_2026\diamonds.csv")
print(recieved_file_content)

column_names = csv_column_reader(recieved_file_content)
print(column_names)