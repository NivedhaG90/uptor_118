# print("hello")
# print("welcome")
# print("welcome to my programming language")
# name = "Meenakshi"
# print(name)
# print(type(name))
# print("testing")

# var = "Mohan"
# print(type(var))

#Mohan - data
# = = Assignemnt operator
#var - object(anything that occupies memory) or variable

# var = 'Mohan'
# print(type(var))

# var = """Mohan"""
# print(type(var))

# var = '900'
# print(type(var))


# var = "Mohan is teaching python \
#          and he is also teaching machine learning"
# print(var)

#triple quotes were called as "Multi Line String"

# var = """Mohan is teaching python\n
#          and he is also teaching machine learning"""
# print(var)

# var = 90
# print(type(var))
#
# var = 90.0
# print(type(var))

# var = 90
# var1 = 90.0
# print(var,"\n",var1)

# var = 90
# print(var)
# var = 99
# print(var)

# var = ["a","b","apple"]
# print(var)
# print(type(var))

# var = ["a","b","apple",1,20]
# print(var)
# print(type(var))

# var = ("a","b","apple",1,20)
# print(var)
# print(type(var))

# var = "a","b"
# print(var)
# print(type(var))

# var = "dhoni" #immutable
# var[4] = "y"
# print(var)

# var = "dhoni"
# var = var.replace ("i","y")
# print(var)

#d - 0
#h - 1
#o - 2
#n - 3
#i - 4

# var = ["d","h","o","n","ashwin"] #mutable
# var[4] = "y"
# print(var)

"""below is the error case as we trying to store y in 4th
    index which is not here"""
# var = ["dhoni"] #mutable
# var[4] = "y"
# print(var)

# var = {"name":"dhoni","place":"ranchi","team":"csk","number":7}
# print(var)
# print(type(var))

# var = {"dhoni","ranchi","csk",7}
# print(var)
# print(type(var))

#below is set which basically removes the duplicates

# var = {"dhoni","ranchi","dhoni",7}
# print(var)
# print(type(var))

# var = {"name":"dhoni","place":"ranchi","team":"csk","number":7}
# print(var["name"])

# var = [{"name":"dhoni","place":"ranchi","team":"csk","number":7},
#        {"name":"Kohli","place":"delhi","team":"rcb","number":18}]
# print(var[1]["name"])

var = {"name":["dhoni","kohli","ashwin"],"place":"ranchi","team":"csk","number":7}
print(var["name"][1])