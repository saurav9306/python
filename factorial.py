def factorial(n):
    res = 1
    for i in range (2, n+1):
        res = res*i
    return res

def binomialCoff(n,r):
    return factorial(n) // (n * factorial(n-r))

n= int(input("enter the value: "))

r = int(input("enter the value of r: "))
print("value of C", n , r, "is", binomialCoff(n,r))
