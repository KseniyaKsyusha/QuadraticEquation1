import math
print("Вирішуємо квадратне рівняння a*x^2 + b*x + c = 0 ")
print("Класичнп программа")
a = float(input("Введіть a = "))
b = float(input("Введіть b = "))
c = float(input("Введіть c = "))
d = b ** 2 - 4 * a * c
print("Дискримінант D = %.2f" % d)
if d > 0:
    x1 = (-b - math.sqrt(d)) / (2 * a)
    x2 = (-b + math.sqrt(d)) / (2 * a)
    print("x1 = %.2f" % x1, "та x2 = %.2f" % x2)
elif d == 0:
    x1 = (-b) / (2 * a)
    print("x1 = %.2f" % x1)
else:
    print("Рішення відсутнє!")
