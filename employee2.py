class Employee:
    def __init__(self, salary):
        self.__salary = salary  

    def get_salary(self):
        return self.__salary
    
    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Invalid salary!")
emp = Employee(25000)
print("Current Salary:", emp.get_salary())
emp.set_salary(30000)
print("Updated Salary:", emp.get_salary())