# Ex11 from the book
# milesPerGallon = int(input("how much fuel does your car use in miles-per-gallon: "))
# litersPerHundKm = milesPerGallon * 0.425144
# print("Your car will use", litersPerHundKm, "liters per hundred KM" )

# Ex32
# x = input("целое четырехзначное число: ")
# sum = 0
# for i in x:
#     sum += int(i)
# print(x[0], "+", x[1], "+", x[2], "+", x[3]," = ",sum)

# Ex33
# x = input("три целых числа: ").split(",")
# print("max number is", max(x[0],x[1],x[2]), "and min number is", min(x[0],x[1],x[2]))

# Ex34
# b = int(input("количество приобретенных вчерашних буханок хлеба: "))
# bread_coast = 3.47
# ybread = 3.47*0.6
# total = b*ybread
# print(f'coast of bread is {bread_coast}$\nsale is 60%\n Total amount is {total}$')

# Ex63
# n = float(input("please type numbers: "))
# print((n * (n + 1) / 2) / n)
    
# numbers = input("please type numbers: ").split(",")
# sum = 0
# for i in range(len(numbers)):
#     print(sum(len(numbers)/len(numbers)))
#     sum+=1

# Ex64
# price = [4.95, 9.95, 14.95, 19.95, 24.95]
# for x in price:
#     print(x, f'{x*0.6:.{2}f}', f'{x-x*0.6:.{2}f}')

# Ex65
temperature_list = [i for i in range(0,101,10)]
print('Celsius\t Farenhayt')
for j in temperature_list:
    print(f'{j} \t {int(9/5*j+32)}')



# Ex66
# price = int(input("tell the price: "))
# while price == "":

