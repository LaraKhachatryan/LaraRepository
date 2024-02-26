# Game 
import random
import os
import msvcrt

monkey_i = random.randint(1,19)
monkey_j = random.randint(1,19)
banana_i = random.randint(1,19)
banana_j = random.randint(1,19)

for i in range(21):
    for j in range(21):
        if monkey_i == i and monkey_j == j:
            print('🐒', end = '')
        elif banana_i == i and banana_j == j:
            print('🍌', end = '')
        else:
            print('🌴', end="")
    print()

