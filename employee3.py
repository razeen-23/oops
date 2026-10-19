
class Employee:
    def __init__(self, name):
        self.name = name

    def calculate_salary(self):
        pass


class FullTimeEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


class PartTimeEmployee(Employee):
    def __init__(self, name, hours, hourly_rate):
        super().__init__(name)
        self.hours = hours
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hours * self.hourly_rate

e1 = FullTimeEmployee("Anu", 30000)
e2 = PartTimeEmployee("Ravi", 80, 200)

print("Full-time Employee:", e1.name)
print("Salary:", e1.calculate_salary())

print("Part-time Employee:", e2.name)
print("Salary:", e2.calculate_salary())