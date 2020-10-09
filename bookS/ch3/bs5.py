def calcsum(a,b,c):
    s=a+b+c
    return s


def average(x,y,z):
    sm=calcsum(x,y,z)
    return sm/3

num1=int(input("Number 1 :"))
num2=int(input("Number 2 :"))
num3=int(input("Number 3 :"))
print("Average of these numbers is ", average(num1,num2,num3))