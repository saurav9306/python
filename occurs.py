"""Read a multi-digit number (as chars) from the console. Develop a program to print
the frequency of each digit with suitable message."""


num = input("Enter a number : ")
print("The number entered is :", num)
uniqDig = set(num)
print(uniqDig)
for elem in uniqDig:
    print(elem, "occurs", num.count(elem), "times")