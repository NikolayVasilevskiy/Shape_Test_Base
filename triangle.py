import math
a = float(input("Введите длину стороны a: "))
b = float(input("Введите длину стороны b: "))
c = float(input("Введите длину стороны c: "))
p = (a + b + c) / 2
s = math.sqrt(p * (p- a) * (p - b) * (p - c))
print("Площадь треугольника: ", s)