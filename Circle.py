import math
class circle():
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * (self.radius**2)
r = int(input("Введите радиус круга: "))
obj = circle(r)
print("Площадь круга:", round(obj.area(), 2))