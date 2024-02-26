# homework 15, ex 173
# id n == "" chashxatec, cragir@ chi haskanum values() function@ 
# def values():
#     n = int(input("Please type a number, in case you want to finish, type 0: "))
#     if n == 0:
#         return 0
#     else:
#         return n + values()
# print(values())

# ex 174
# def gcd(a, b):
#     if b == 0:
#         return a
#     if a == b:
#         return a
#     if a > b:
#         a = a - b
#     else:
#         b = b - a
#         return b
# a = int(input("Enter the first integer: "))
# b = int(input("Enter the second integer: "))
# print(f'GCD of {a} and {b} is equale', gcd(a,b))


# def gcd(a, b):
#     i = 1
#     small = min(a,b)
#     for i in range(1, small + 1):
#         if (a % i == 0) and (b % i == 0):
#             gcd_result = i
#     return gcd_result
# print (gcd(60,48))

