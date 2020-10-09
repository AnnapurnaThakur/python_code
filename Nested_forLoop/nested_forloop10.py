a=int(input("Enter a number : "))
for i in range(a,1,-1):
    for j in range(1,i+1):
        print(" " , end="")
    for k in range(i-1,a,1):
        print(k , end="")
    print()


    
#     Enter a number : 7
#        6
#       56
#      456
#     3456
#    23456
#   123456