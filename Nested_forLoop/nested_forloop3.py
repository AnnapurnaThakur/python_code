
#1
#22
#333
#4444
#55555
#666666

a=int(input("Enter a number : "))
for i in range(1,a+1):
    print("#",end="")
    for j in range(1,i+1):
        print(i, end="")
    print()
