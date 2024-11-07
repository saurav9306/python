from math import sqrt
mylist = []
num = int(input("enter the number of element"))
for i in range (num):
    val=int(input("enter your element"))
    mylist.append(val)
print("the lemght of the list is: ", len(mylist))
print("list contents: ", mylist)
total = 0
for elem in mylist:
    total += elem
    mean = total / num
total = 0
for elem in mylist:
    total += (elem - mean) * (elem - mean)
    variance = total / num
stdDev = sqrt(variance)
print ("mean = ", mean)
print ("variance = ", variance)
print("standard = ", stdDev)