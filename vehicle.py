class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)


class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors

    def display(self):
        super().display()
        print("Number of doors:", self.doors)


class Bike(Vehicle):
    def __init__(self, brand, model, type):
        super().__init__(brand, model)
        self.type = type

    def display(self):
        super().display()
        print("Bike type:", self.type)

car = Car("Toyota", "Innova", 4)
bike = Bike("Yamaha", "R15", "Sports")

print("Car Details:")
car.display()

print("\nBike Details:")
bike.display()