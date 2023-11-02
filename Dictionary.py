# student = {
#     "name": "Alice",
#     "age": 25,
#     "grade":"A"
# }
# name = student["name"]
# print(name)

# age = student["age"]
# print(age)

# # Adding a new key-value pair
# student["city"] =  "New York"

# # modifying a value 
# student["age"] = 26
# print(student)


# # Iterating Through the dictionary
# for key, value in student.items():
#     print(f"{key}:{value}")


# c = {num:num**3 for num in range(1,6)}
# print(c)


# c = student.get("age")
# print(c)


# dict = {0:10 ,1:20}

# dict[2] = 30
# print(dict)

# dict1 = {0:10 ,1:20}
# dict2 = {3:30 ,4:40}
# dict3 = {5:50 ,6:60}

# dict1.update(dict2)
# dict1.update(dict3)

# print(dict1)







# d = {'x':10 , 'y':20 , 'z':30}

# for key , value in d.items():
#     print(f"{key}:{value}")


# dict = {num: num*num for num in range(1,8)}
# print(dict)


# dict1 = {x: x**2 for x in range(1,16)}
# print(dict1)


# my_dict = {'data1': 100, 'data2':-54, 'data3':247}
# print(sum(my_dict.values()))
    

# colour_dict = {'red': '#FF0000',
#                'green': '#008000',
#                'black': '#000000',
#                'white': '#FFFFFF',}

# for keys in sorted(colour_dict):
#     print("%s: %s" % (keys, colour_dict[keys]))




d = {1:10 , 2:20 , 3:30 , 4:40 , 5:50 , 6:60}

n = int(input("enter a key : "))

if n in d:
    print("yes given key is exist in d")

else:
    print("not exist") 
