# homework6
# # Ex1
# for i in range(0,11):
#     if i%2 == 0: print(i, end='')
#     print(' ', end='')
# print('\n')
# for i in range(1,12):
#     if i%2 == 1: 
#         print(i, end='')
#     print(' ', end='')
# print('\n')
# for i in range(2, 13):
#     if i%2 == 0: print(i, end='')
#     print(' ', end='')
# print('\n')
# for i in range(3, 14):
#     if i%2 == 1:
#         print(i, end='')
#     print(' ', end='')
# print('\n')
# for i in range(4, 15):
#     if i%2 == 0:
#         print(i, end='')
#     print(' ', end='')
# print('\n')
# for i in range(5, 16):
#     if i%2 == 1:
#         print(i, end='')
#     print(' ', end='')
# print('\n')

# 2nd var------------------
# x = 0
# y = 12
# for i in range(6):
#     for j in range(x,y,2):
#         print(j,end = '\t')
#     print('\n')
#     x+=1
#     y+=1

# Ex2
# for i in range(0,6):
#     for j in range(0,i):
#        print(i, end='\t')
#     print('\n')   

# # Ex3
# a = int(input("height: "))
# b = int(input("length: "))
# for i in range(a):
#     print("|", end='')
#     for j in range(b):
#         if i == 0 or i == a-1:
#            print("-", end='')
#         else:
#            print(" ", end='')
#     print("|", end="\n")
      
# Ex5
# num_seq = int(input('Сколько чисел в последовательности: ')) 
# num_count = 0 
# for i in range(1, num_seq + 1): 
#        number = int(input('Введите число: ')) 
# for j in range(2, number): 
#     if number % j == 0: 
#      break 
#     else: 
#      num_count += 1 
# print('Простых чисел в последовательности', num_count)

# Ex6
# N = int(input("enter a number: "))
# factorial = 1
# sum = 0
# for i in range(1, N+1):
#    factorial *= i
#    sum += factorial
# print(sum)

# Ex8
# h = int(input('Высота пирамиды: '))
# for j in range(1, h+1):
#   for i in range(h+1):
#     if i == h:
#       print('#' * (j * 2 - 1), end = "")
#       h -= 1
#     else:
#       print(' ', end = "")
#   print()

# var2
# height = int(input("Enter the height of the equilateral triangle: "))
# if height <= 0:
#     print("Height must be a positive integer.")
# else:
#     for i in range(1, height + 1):
#         spaces = " " * (height - i)
#         hashtags = "#" * (2 * i - 1)
#         print(spaces + hashtags)


    





