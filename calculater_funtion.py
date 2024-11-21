a= int(input("enter your 1's number"))
b= int(input("enter your 2'nd number"))


def add(a,b):
    return a+b
    
def sub(a,b):
    return a-b
def mult(a,b):
    return a*b
def divi(a,b):
    return a/b,a%b

print("select any of the opperater:")
opt=input("+, -, *, /, %:  ")

while True:

    if(opt == '+'):
        print(add(a,b))

    elif(opt == '-'):
        print(sub(a,b))

    elif(opt == '*'):
        print(mult(a,b))
    
    elif(opt == '/'):
        print(divi(a,b))

    else:
        print("invalid input")
    break