class car:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price

s1 = car("suzuki","alto",4000000)
s2 = car("suzuki","wagon r",800000)
s3 = car("suzuki","swift",9000000)

print("car 1 details:")
print("brand:",s1.brand)
print("model:",s1.model)
print("price:",s1.price)

print("car 2 details:")
print("brand:",s2.brand)
print("model:",s2.model)
print("price:",s2.price)

print("car 3 details:")
print("brand:",s3.brand)
print("model:",s3.model)
print("price:",s3.price)