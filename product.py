class Product:
    def __init__(self, name,price,quantity):
        self.name = name
        self.price=price
        self.quantity=quantity

    def display(self):
        total=self.price*self.quantity
        print("product details")
        print("Name:", self.name)
        print("price:",self.price)
        print("quantity:",self.quantity)
        print("total price =",total)

name = input("Enter your product name:")
price = int(input("enter your price:"))
quantity=int(input("enter your quantity:"))

p =Product(name,price,quantity)
p.display()