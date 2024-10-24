from datetime import date

name = input("enter your name: ")
DOB = int(input("enter your your year of birth: "))
cyear= date.today().year
age = cyear - DOB
if(age > 60):
    print(name, " is a honerd senior citizon of india")
else:
    print(name, "is not a senior citizon")
