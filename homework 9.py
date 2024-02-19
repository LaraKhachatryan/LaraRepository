# Lesson 16
# Ex1

# theDict = {'Aram':4, 'Inga':3, 'Tsovinar':2, 'Gagik': 1}
# myValues = list(theDict.values())
# myValues.sort()
# valuse_list = ['Gagik', 'Tsovinar', 'Inga', 'Aram']
# values_sorted = {}
# for i, j in zip(valuse_list, myValues):
#     values_sorted[i] = j
# print(values_sorted)

# Ex2

# my_dict = {1:'Gagik', 2:'Tsovinar', 3: 'Inga', 4:'Aram'}
# my_dict["Poghos"] = 5
# print(my_dict)

# Ex3 - sxal patasxan, chem haskanum inchn e sxal 
# my_dict = {1: 'A', 2:'B', 3:'C', 4:'D'}
# my_dict_list = list(my_dict.keys())
# i = input("Type a Key: ")
# if i in my_dict_list:
#     print("already exists")
# else:
#     print("Does not exist")

# Ex4
# dict1 = {'a':50, 'b':70}
# dict2 = {'c':400, 'd':600}
# dict1.update(dict2)
# print(dict1)

# Ex5
# my_dict = {'a':1, 'b':2, 'c':3, 'd':4}
# my_list = list(my_dict.values())
# num = int(my_list[3])
# multi = 1
# for i in range(1, num+1):
#     multi = multi*i
# print(multi)

# Ex6
# my_dict = {'D': 56, 'E': 12, 'F': 69, 'C': 45, 'B': 23, 'A': 67}
# list_values = list(my_dict.values())
# list_values.sort(reverse=True)
# print(list_values)
# print(list_values[1:4])

#Lesson 18
# Ex1
# my_dict = {'Ann': 1, 'Andy':5, 'Bob': 10, 'Rachel':9,
# 'Elsa': 2, 'Ted':3, 'Tod': 7, 'Rachel':4, 'Sally': 6, 'Stella':8 }
# print(my_dict)

# Ex2
# my_dict = {'Ann': 10, 'Andy':5, 'Bob': 10, 'Rachel':9, 'Elsa': 8, 'Ted':7, 'Tod': 7, 'Rachel':9, 'Sally': 6, 'Stella':8 }
# total_rating = sum(my_dict.values())
# quantity_of_students = len(my_dict)
# average_rating = total_rating/quantity_of_students
# print(average_rating)

# Ex3
# my_dict = {'Ann': 'good', 'Andy': 'bad', 'Bob': 'good', 'Rachel': 'bad', 'Elsa': 'good', 'Ted': 'bad', 'Tod': 'good', 'Rachel': 'bad'}
# key_list = list(my_dict.keys())
# for student in key_list:
#     if student in my_dict:
#         print(f'{student} is a {my_dict[student]} student')

