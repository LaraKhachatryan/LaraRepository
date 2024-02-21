import math

def calculate_hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

def main():
    a = float(input("Введите длину первого катета: "))
    b = float(input("Введите длину второго катета: "))

    c = calculate_hypotenuse(a, b)
    
    print("Длина гипотенузы:", c)

main()