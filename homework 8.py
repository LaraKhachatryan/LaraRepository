# Lesson14 Ex1
# list = ('a', '99', True, False, '##', "5.88", "ABC", "   " )
# print(list)

# Ex2
# my_list = [ "HP", "Asus", "DELL", "MAC", "Lenovo"]
# for i in my_list:
#     if(i == "MAC"):
#         print(True)

# Ex3
# password = input("type your password: ")
# a, b, c, d = 0, 0, 0, 0
# capitalalphabets = "ABCDEFGHIJKLMNOPQRSTUVW"
# smallalphabets = "abcdefghijklmnopqrstuvwxyz"
# digits = "0123456789"
# specialchars = "!@#$%"
# if len(password) >= 8:
#     for i in password:
#         if i in capitalalphabets:
#            a+=1
#         if i in smallalphabets:
#             b+=1
#         if i in digits:
#             c+=1
#         if i in specialchars:
#             d+=1
# if(a >= 2 and b >= 2 and c >= 2 and d >= 2 and a+b+c+d == len(password)):
#     print("strong")
# else:
#     print("weak")

# Ex4
# def get_text_after_equal_sign(link):
#     parts = link.split('=')
#     if len(parts) > 1:
#         text_after_equal_sign = parts[-1]
#         return text_after_equal_sign
#     else:
#         return None 
# link = input("Enter a link: ")
# text_after_equal_sign = get_text_after_equal_sign(link)
# if text_after_equal_sign is not None:
#     print("Link id is equle = ", text_after_equal_sign)
# else:
#     print("No id found")

# Ex5
# word = input("type a word: ")
# reverse = word[::-1]
# if word == reverse:
#     print("OPEN")
# else:
#     print("Trash")

# Ex6
# text = "hello, how are you ?"
# myList = text.split(" ")
# print(myList)

# Ex7
# numbers = input("type 5 numbers: ").split(",")
# for i in numbers:
#     if int(i)%2 == 0:
#         print(i, end=" ")

# Ex8
# numbers = input("write numbers: ").split(" ")
# for i in numbers:
#     if int(i)%2 != 0:
#         print(i, end=" ")

# # Ex9
# import random
# my_list1 = ["Armen", "Elsa", "Lily", "Ashot", "Edik"]
# my_list2 = ["Armen", "Elsa", "Lily", "Ashot", "Edik"]
# random.shuffle(my_list2)
# for i in my_list1:
#     for j in my_list2:
#         if i != j:
#             print(f'{i} s grandson is {j}')
#             my_list2.remove(j)
#             break
#         else:
#             continue

# Ex10
# list = ["1", "2", "2", "5", "5", "6"]
# unique_list = []
# for i in list:
#     if i not in unique_list:
#         unique_list.append(i)
# print(unique_list)

# Lesson14
# Ex1
# my_list = [1,2,3,4,5]
# num = int(my_list[4])   
# sum = 0
# for i in range(1, num + 1):
#     sum = sum + i
# print(sum)

# Ex2
# my_list =[1, 2, 3, 4, 5]
# num = int(my_list[4])
# mult = 1
# for i in range(1,num+1):
#     mult = mult*i
# print(mult)

# Ex3
# my_list = ["hello", "!", "how", "are", "you", "?"]
# max_string = max(my_list, key=len)
# print("The largest string is:", max_string)

# Ex4
# list1 = [1, 2, 3, 4, 5, 6,]
# list2 = [5, 3, 88, 11, 95]
# for i in list1:
#     if i not in list2:
#         print(False)
