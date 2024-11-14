num =input("enter a mult digite number : ")
freq = {}
for i in num:
    if i.isdigit():
        if i in freq :
            freq[i] += 1
        else:
            freq[i] = 1

print("frequency of each digit: ")
for key, value in freq.items():
    print("{} - {}".format(key,value))
56464