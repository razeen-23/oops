class employee:
    def __init__(self,salary):
        self.salary = salary

    
    def increase_salary(self,percentage):
        self.salary += self.salary * percentage / 100

    def display_salary(self):
        print("updated salary:",self.salary)

salary=float(input("enter employee salary:"))
percentage=float(input("enter increase percentage:"))

emp = employee(salary)
emp.increase_salary(percentage)
emp.display_salary()

