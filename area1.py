import math

class Circle:
    def area(self):
        r = 5
        return math.pi * r * r


class Rectangle:
    def area(self):
        length = 10
        width = 5
        return length * width


class Triangle:
    def area(self):
        base = 8
        height = 4
        return 0.5 * base * height

c = Circle()
r = Rectangle()
t = Triangle()

print("Circle area:", round(c.area(), 2))
print("Rectangle area:", r.area())
print("Triangle area:", t.area())