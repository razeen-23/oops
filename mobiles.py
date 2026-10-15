class Mobile:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print("Mobile Name:", self.name)
        print("Price:", self.price)
        print("--------------------")


mobiles = []

# Get details of five mobiles
for i in range(5):
    print("\nEnter details of mobile", i + 1)

    name = str(input("Enter mobile name: "))
    price = int(input("Enter mobile price: "))

    mobile = Mobile(name, price)
    mobiles.append(mobile)

# Display mobiles costing more than 20000
print("\nMobiles costing more than 20000:")
print("====================")

for mobile in mobiles:
    if mobile.price > 20000:
        mobile.display()
    else:
        print("cost less than 20000")
        print("^^^^^^^^^^^^^^^^^^^")
       
        mobile.display()