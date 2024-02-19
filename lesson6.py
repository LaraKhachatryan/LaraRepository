# ------------------------------------------------
# n1, n2 = 0, 1
# for i in range(int(input('Enter number: '))):
#     print(n1)
#     n1, n2 = n2, n1 + n2
# ------------------------------------------------
# boy = int(input('Enter boys count: '))
# girl = int(input('Enter girls count: '))
# text = ''
# if boy == girl:
#     for i in range(boy):
#         text += 'BG'
# elif girl == boy - 1:
#     for i in range(girl):
#         text += 'BG'
#     text += 'B'
# elif boy == girl - 1:
#     for i in range(boy):
#         text += 'GB'
#     text += 'G'
# elif boy == girl - 2:
#     for i in range(boy):
#         text += 'BG'
#     text = 'G' + text[:len(text) // 2] + 'G' + text[len(text) // 2:]
# elif girl == boy - 2:
#     for i in range(girl):
#         text += 'GB'
#     text = 'B' + text[:len(text) // 2] + 'B' + text[len(text) // 2:]
# print(text)
# ------------------------------------------------
# text = input('Enter text: ')
# number_count = 0
# letter_count = 0
# char_count = 0
# for i in text:
#     if i.isdigit():
#         number_count += 1
#     elif i.isalpha():
#         letter_count += 1
#     else:
#         char_count += 1
# print(f'Number count -> {number_count}\nLetter count -> {letter_count}\nChar count -> {char_count}')
# ------------------------------------------------
# for i in range(1, 7):
#     print(i)
# ------------------------------------------------

# i = 1
# while i <= 7:
#     print(i)
#     i += 1
# ------------------------------------------------

# while True:
#     number = int(input('Enter number: '))
#     if number == 0:
#         break
#     else:
#         print(number)
# ------------------------------------------------

# kassa = 0
# while True:
#     age = int(input('Write your age: '))
#     if age == 0:
#         break
#     elif 0 < age <= 2:
#         continue
#     elif 2 < age <= 12:
#         kassa += 14
#     elif 12 < age <= 65:
#         kassa += 23
#     elif age > 65:
#         kassa += 18
#     else:
#         print('Sxal mutq!!!')
#     print(kassa)
# print(kassa)
# ------------------------------------------------
        

# import random

# for i in range(10):
#     text = ''
#     while True:
#         char = random.choice('OP')
#         text += char
#         if len(text) >= 3:
#             if text[-1] == text[-2] == text[-3]:
#                 print(f'{text} (попыток: {len(text)})')
#                 break

# ------------------------------------------------

# import random

# for i in range(10):
#     O_count = 0
#     P_count = 0
#     text = ''
#     while True:
#         char = random.choice('OP')
#         text += char
#         if char == 'O':
#             O_count += 1
#             P_count = 0
#         else:
#             P_count += 1
#             O_count = 0
#         if O_count == 3 or P_count == 3:
#             print(text)
#             break
# ------------------------------------------------
# n = int(input('tiv:  '))

# for i in range(1 , n + 1):
#     for _ in range(i):
#         print(i, end=' ')
#     print()
# # ------------------------------------------------
# n = int(input('tiv:  '))
# for i in range(n + 1):
#     for j in range(n + 1):
#         if i == j:
#             print('^', end='')
#         elif n == i + j:
#             print('^', end='')
#         else:
#             print(' ', end='')
#     print()
# ------------------------------------------------
# name = input("please type your name: ")
# char_number = len(name)
# print("your name has", char_number, "char numbers")

# limit = int(input("введите целов число: "))
# for i in range(3,limit+1,3):
#     print(i)

# Ex63
n = int(input("number: "))
while n != 0:
    n = (int(input("number: "))):
    for i in range(n)
