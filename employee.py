class employee:
    def __init__(self,name,emp_id,salary):
        self.name=name
        self.emp_id=emp_id
        self.salary=salary

    def display(self):
        print("employee name",self.name)
        print("employee id",self.emp_id)
        print("employee salary",self.salary)

name = input("enter employee name: ")
emp_id = input("enter employee id: ")
salary = float(input("enter employee salary:"))

e = employee(name,emp_id,salary)
e.display()

      


