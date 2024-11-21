list = []
n = int(input('enetr the size of list: '))
for i in range(0,n):
    num= int(input("enter a number: "))
    list.append(num)
for index, item in enumerate(list):
    print("index:", index, "value:", item)