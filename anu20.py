# a=int(input("Enter a number : "))
# for i in range (0,6):
#     for j in range(0,i):
#         print(j)
#     print(i)


# a=int(input("Enter a number : "))
# for i in range(1,a+1,2):
#     for j in range(1,i+2,2):
#         print(j, end=" ")
#     print()

# a=int(input("Enter a number : "))
# for i in range(0,a+1):
#     for j in range(0,i,1):
#         print(i, end=" ")
#     print()


# a=int(input("enter a number : "))
# for i in range (a,0,-1):
#     for j in range(1,i+1):
#         print(a, end="")
#     print()


# a=5+-3
# print(a)


# a=4
# for i in range(1,a+1):
#     for j in range(1,i+1):
#         print (j, end="")
#     print()
# b=3
# for h in range(b,0,-1):
#     for k in range(1,h+1):
#         print(k , end="")
#     print()


# a=int(input("Enter a number : "))
# b=1
# for i in range(a):
#     for j in range(1,6):
#         print(b, end="")
#     print()
#     b=b+1

a=int(input("Enter a number : "))
for i in range(a,0,-1):
    for j in range(i):
        print(i, end="")
    print()
