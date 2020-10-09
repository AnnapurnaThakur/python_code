print("more than 6 digit password- Atlist 1 capital leter, 1 small leter, 1 number and 1 special charector")
a=input("Enter your Password : ")
print()
b=len(a)
p1='t'
p2='t'
p3='t'
p4='r'
p5='t'
if b>=6:    
    for i in a:        
        if i.isupper()==True:
            p1='s'
        if i.islower()==True:
            p2='t'
        if i.isdigit()==True:
            p3='a'
        if i.isspace()==True:
            p4='t'
        if i=='@' or i=='!' or i=='$' or i=='%' or i=='#' or i=='*':
            p5='t'
        check=p1+p2+p3+p4+p5                    
    if check=="start":
        while True:
            r=input("Please Renter same  password : ")        
            if r==a:
                print("You Entered successfully ")
                print("Welcome to the class")  
                break
            else:
                print()                              
    else:
        print("Sorry your password is incorrect")          
else:
    print("Please enter above 6 digit or above 6 digit password")
