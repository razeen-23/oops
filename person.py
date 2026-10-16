class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Person's Details")
        print("Name:", self.name)
        print("Age:", self.age)


name = input("Enter your name: ")
age = int(input("Enter your age: "))

p = Person(name, age)
p.display()

        
        