import random
import os
import msvcrt

crab_i = random.randint(1, 19)
crab_j = random.randint(1, 19)
worm_i = random.randint(1, 19)
worm_j = random.randint(1, 19)
points = 0
while True:
    for i in range(21):
        for j in range(21):
            if i == crab_i and j == crab_j:
                print('🦀', end='')
            elif i == worm_i and j == worm_j:
                print('🐣', end='')
            else:
                print('🌊', end='')
        print()
    print(f'Points -> {points}')
    move = msvcrt.getwch().upper()
    if move == 'W':
        crab_i -= 1
    elif move == 'S':
        crab_i += 1
    elif move == 'A':
        crab_j -= 1
    elif move == 'D':
        crab_j += 1
    elif move == 'Q':
        break
    if crab_i == worm_i and crab_j == worm_j:
        worm_i = random.randint(1, 19)
        worm_j = random.randint(1, 19)
        points += 1
    os.system('cls')
# --------------------------------------------------
# n = 5
# fact = 1
# for i in range(1, n + 1):
#     fact *= i
# print(fact)
# --------------------------------------------------
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
# print(factorial(5))
# --------------------------------------------------
# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n - 2) + fib(n - 1)
# print(fib(7))
# --------------------------------------------------
# def summary():
#     n = int(input("type the number: "))
#     if n == 0:
#         return 0
#     else:
#         return summary() + n
# print(summary())    
# --------------------------------------------------
# 4 - 100
# def binary(num):
#     if num <= 1:
#         return str(num)
#     txt = ''
#     txt += str(num % 2)
#     return str(binary(num // 2) + txt)
# print(binary(18))

# --------------------------------------------------

# def binary(num):
#     if num == 1:
#         return str(num)
#     return binary(num // 2) + str(num % 2)
# #           binary(9) + '0'
# #           binary(4) + '10'
# #           binary(2) + '010
# #           binary(1) + '0010
# #           '10010
# print(binary(18))

# --------------------------------------------------
# def func(mylist):
#     if mylist == []:
#         return []
#     else:
#         return [mylist[0]]*mylist[1] + func(mylist[2:])
# mylist =  ["A", 12, "B", 4, "A", 6, "B", 1]
# print(func(mylist))
# --------------------------------------------------

# def encode(mylist, count=1):
#     if len(mylist) == mylist.count(mylist[0]):
#         return [mylist[0], mylist.count(mylist[0])]
#     if mylist[0] == mylist[1]:
#         return encode(mylist[1:], count + 1)
#     else:
#         return [mylist[0], count] + encode(mylist[1:], count=1)
# mylist = ["A", "A", "A", "A", "A", "A", "A", "A", "A","A", "A", "A", "B", "B", "B", "B", "A", "A", "A", "A", "A", "A", "B", "B"]
# print(encode(mylist))
# --------------------------------------------------
