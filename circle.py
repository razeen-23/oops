class circle:
    def __init__(self,radius):
        self.radius= radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def circumtance(self):
        return 2 * 3.14 * self.radius
    
radius = float(input("enter radius:"))
c = circle(radius)

print("area of a circle:",  c.area())
print("Circumference of circle:", c.circumtance())

    



    
