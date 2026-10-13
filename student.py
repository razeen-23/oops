# class student:
#     def__init__(self,name,age,course)
#     self.name=Name 
#     self.age=age
#     self.course=Course 
# s1 = student("razeen",26,"computer science")
# s1.print()

class Student:
    def __init__(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course

s1 = Student("razeen",20,"computer science")

print("student name:",s1.name)
print("student age:",s1.age)
print("student course:",s1.course)
