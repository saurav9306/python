name = input("enter student's name: ")
USN= input("enter student's USN number: ")
eng= int(input("enter student's english marks: "))
maths = int(input("enter student's maths marks: "))
chem = int(input("enter student's chemistry marks: "))
print("===============================================")
print(name)
print(USN)
total = eng + maths + chem
print("Total marks abtained by the staudent: ",total)
perage= (total / 300) * 100
print("percentage of the student: ",perage)