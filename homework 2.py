import math
x=input("Please type two points on the Earth’s surface": ).split(",")
y=input("Please type another two points on the Earth’s surface": ).split(",")
print(int(6371.01*math.acosh(math.asin(x[0])*math.asin(y[0])+math.acos(x[0])*math.acos(y[0])*math.acos(x[1]-y[1]))))