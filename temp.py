class temp:
    def __init__(self,celxius,farnt):
        self.celxius=celxius
        self.farnt=farnt

    def conv_to_celsius(self):
        return(self.farnt - 32) * 5 / 9

    def conv_to_fahrenheit(self):
        return(self.celxius * 9/5) + 32

celxius=float(input("enter the celsius:"))
farnt=float(input("Enter the fahrenheit:"))

t=temp(celxius,farnt)
print("*****************")
print("fahrenheit to celsius =",t.conv_to_celsius())
print(" celsiu to fahrenheit =",t.conv_to_fahrenheit()) 

