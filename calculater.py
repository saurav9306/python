a= int(input("input enter your 1st numberf: "))
b= int(input("input enter your 2nd numberf: "))
print("select the any operator")
opt= input("+, -, *, /, //, %")

res= 0

if(opt== "+"):
    res = a + b
    print(res)

elif(opt == "-"):
    res = a-b
    print(res)

elif(opt == "*"):
    res = a*b
    print(res)

elif(opt == "/"):
    res = a/b
    print(res)

elif(opt == "//"):
    res = a//b
    print(res)

elif(opt == "%"):
    res = a%b
    print(res)
else:
    print("invalid input")
