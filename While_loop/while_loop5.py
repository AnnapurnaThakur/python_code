#     1
#    212
#   32123
#  4321234
# 543212345

a= int(input("Enter a number : "))
x=1
for i in range(a,1,-1):
   
    for j in range(1,i):
        print(" " , end="")
    for k in range(1,x+1):
        print("*" , end=" ")
    print()
    x+=1

# x=1
# for i in range(a,1,-1):
    
#     for j in range(1,i):
#         print(" " , end="")
#     for k in range(x,0,-1):
#         print(k , end="")
#     print()
#     x+=1


x=1
for i in range(a,1,-1):
    for j in range(1,i):
        print(" " , end="")
    for k in range(x,0,-1):
        print(k , end="")
    x+=1
    y=x
    for l in range(2,y):
        print(l, end="")
    print()


