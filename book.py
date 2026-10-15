class books:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    
    def display(self):
        print("*****************")
        print("book name:   ",self.title)
        print("Author name: ",self.author)
        print("Price :      ",self.price)
        print("*****************")
print("enter your book information")
title=input("Enter YOUR book title:")
author=input("Enter the author:")
price=int(input("enter the price:"))

book1=books(title,author,price)



book1.display()
