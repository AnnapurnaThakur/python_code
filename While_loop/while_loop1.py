# 1
# 1 2
# 1 2 3
# 1 2 3 4


a=int(input("Enter a number : "))
x=1;
y=1;
while x<a+1:
    while y<x+1:
        print(y ,end=" ")
        y=y+1
    print()
    x=x+1
    y=1
