#Dictionary - Travels by keys
# var = {"name" : "Nivedha", "age": 32, "place":"Chennai"}
# print(var)
#
# for x in var:
#     print(x)
#
# for x in var.items():
#     print(x) #Prints as Tuples
#
# for x in var.values():
#     print(x)

# for x in var:
#     if x == "age":
#         print("Success")
#         break
#     else:
#         print("failure")

# for x in var:
#     if x == "age":
#         continue
#     else:
#         print("failure")

# for x in var:
#     if x == "age":
#         continue
#     elif x == "place":
#         continue
#     else:
#         print("failure")

# for x in var:
#     if x == "age" or x == "place":
#         continue
#     else:
#         print("failure")
#
# for x in var:
#     if x in ("age","place"):
#         continue
#     else:
#         print("failure")

# for x in var:
#     if x in ["age","place"]:
#         continue
#     else:
#         print("failure")

# for x,y in var.items():
#     print(x)
#     print(y)
#
# for x,y in var.items():
#     print("Key is {x}, Value is {y}") #check the recording
#
# for x, y in var.items():
#     print(f"Key is '{x}', Value is '{y}' ")

# var = {"name" : ["Nivedha"], "age": [32], "place":["Chennai"]}
# print(var)
# print(type(var))
# #In data science, we need input in data frame format
# import pandas
# df = pandas.DataFrame(var)
# print(df)
# print(type(df))
# print(df.ndim) #dimension

# single dimension data:
# name    age
# Nivedha 32
# Riya    12
#
# Two Dimension data: Always data in files like csv will be 2 dimension data
#       name     age
# 0     Nivedha  32
# 1     Riya     12

# Pandas is library that can be used for creating or converting the following
# 1. Single Dimension Data (Series)
# 2. Double Dimension Data (Dataframe)
# 3. Multi Dimension Data (Panels)
# Pandas is mainly used for converting to a dimensional data


#csv - light weighted file compared to excel. Comma separated value. Csv files can be easily opened in any editor.
# Excel cannot be opened in any editor. If u send an excel to a client who doesnt have ms office,
# it will be difficult for him to open it. Whereas if u send as csv, he can open it by editor also.
# import pandas
# df = pandas.read_csv("diamonds.csv")
# print(type(df))
# print(df.ndim)

# var = {"name":["Nivedha"]},{"name1":["Riya"]}
# print(var)
# print(type(var))
# print(type(var[0]))

var = "Nivedha"
print(dir(var)) #Returns the functions available for string

var = ["Nivedha"]
print(dir(var)) #dir - directory. Returns the functions available for list

var = {"name":["Nivedha"]}
print(dir(var)) #dir - directory. Returns the functions available for dictionary

var = "Nivedha"
print(var.upper())

#
# #String - travels by each char
# var = "Nivedha"
# print(var)
#
# for x in var:
#     print(x)
#
# #List - Travels by comma separator
# var = ["Nivedha", "age", "Chennai"]
# print(var)
#
# for x in var:
#     print(x)
#
