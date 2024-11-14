num1= int(input("enter your 1st number"))
num2= int(input("entyer your 2nd number"))
num3= int(input("enter your 3rd number"))

if (num1>num2 and num1>num3):
    print(num1," is the gretest number")
elif(num2>num1 and num2>num3):
    print(num2," is the gretest number")
else:
    print(num3," is the gretest number")