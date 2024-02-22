# Ex85
# import math

# def calculate_hypotenuse(a, b):
#     return math.sqrt(a**2 + b**2)

# def main():
#     a = float(input("Введите длину первого катета: "))
#     b = float(input("Введите длину второго катета: "))

#     c = calculate_hypotenuse(a, b)
    
#     print("Длина гипотенузы:", c)

# main()

# def drawBox():
#   print("**********")
#   print("*        *")
#   print("*        *")
#   print("**********")
# drawBox()

# def drawBox(width, height, outline, fill):
#  # Слишком маленькие прямоугольники не могут быть нарисованы при помощи этой функции
#  if width < 2 or height < 2:
#      print("Ошибка: ширина или высота прямоугольника слишком малы.")
#  quit()
# def drawBox(1, 5, "@", ".")
    
#  # Рисуем верхнюю линию прямоугольника
#  print(outline * width)
#  # Рисуем стороны прямоугольника
#  for i in range(height – 2):
#  print(outline + fill * (width – 2) + outline)
#  # Рисуем нижнюю линию прямоугольника
#  print(outline * width)
# # Демонстрируем работу обновленной функции
# drawBox(14, 5, "@", ".")

# def pillars(num_pill, dist, width):
#     if num_pill <= 1:
#         total_distans = 0
#     else:
#         dist*=100
#         total_distans = ((num_pill -1)*dist) + ((num_pill-2)*width)
#     return total_distans
# pillars(1, 10, 10)
# pillars(2, 20, 25)
# pillars(11, 15, 30)

# def multiply(n):
#     if n == 0:
#         return 0
#     elif n < 0:
#         power = abs(n)
#     if n<0:
#         power = -power
#     print(n*(5**power))
# # multiply(5)

# line=input("").split()
# cnt=0
# for i,s in enumerate(line):
#     if s.isdigit():
#         cnt+= len(s) # считаем цифры
# if cnt == 0:
#     print("числа не обнаружены")
# else:
#     print("",cnt)

# def multiply(n):
#     number = str(n)
#     cnt = 0
#     for i in number:
#         if i.isdigit():
#             cnt+=1
#     print(cnt)
# multiply(100)

# def multiply(n):
#   print( n*5**len(str(abs(n))) )
# multiply(100)