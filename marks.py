class marks:
    def __init__(self,mark1,mark2,mark3):
        self.mark1=mark1
        self.mark2=mark2
        self.mark3=mark3

    def total(self):
        return  self.mark1 + self.mark2 + self.mark3

    def average(self):
        return self.total()/3

    def grade(self):
        if self.mark1>=18 and self.mark2>=18 and mark3>=18:
            return "pass"
        else:
            return "fail"

        

mark1=int(input("enter your mark1:"))
mark2=int(input("enter your mark2:"))
mark3=int(input("enter your mark3:"))

p = marks(mark1, mark2,mark3)

print("total mark:",p.total())
print("average:",p.average())
print("grade:",p.grade())




  
        




