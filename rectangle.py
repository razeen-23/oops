class rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

length=float(input("enter the length:" ))
width=float(input("enter the width:" ))
    
rect = rectangle(length,width)
print("area of a rectangle:", rect.area())
