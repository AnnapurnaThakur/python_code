print("Soap         price 50rs.   point: 1")
print("Shampoo      price 150rs.  point: 1.5")
# print("Facewash     price 99rs.   point: 2")
# print("Cream        price 98rs.   ponit: 1")
# print("Hair oil     price 350rs.  point: 2.5")
# print("Body lotion  price 100rs.  point: 3")
import sys
a1="soap"
b1="shampoo"
print("press 1 for soap  ")
print("press 2 for shampoo  ")
a=int(input("Select your choose : "))
b=int(input("How many products you want : "))
if a==1:
    print(a1)
    print("total amount =" ,50*b)
    print("you will get" , 1*b ,"ponits")
    c=1*b
    if c==10:
        print("you will get 50 rs.")
    elif c<10:
        print("your point is less than 10")
    elif c==20:
        print("you will get 100rs.")
    elif c<21:
        print("you will get only 50 for 10 points, now you have ", 1*b-10 ,"points" )
    elif c>20:
        print("You will get 50 for 10 points, now you have"  ,1*b ,"ponit")
    else:
        print("you have less than 10 ponits so no money can be given to you ")
else:
    d=input("You want to continue : (Y/N)")
    if d=='Y' or d=='y':
        
            sys.exit(0)

        





    
