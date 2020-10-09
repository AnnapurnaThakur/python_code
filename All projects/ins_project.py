#User Login
u=input("Enter your user name ")
#password
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
            ad1="Anu Kumari"
            ad2="123Anu@"
            ca1="Souvik"
            ca2="123Souvik@"
            ua1="User"
            ua2="123User@"

            if a==ad2 and u==ad1:
                print("You Entered successfully ")
                print("Welcome to Asansolution As a Admin / Developer")  
                break
            elif a==ca2 and u==ca1:
                print("You Entered successfully ") 
                print("Welcome to client Admin")
                #Admin create Package
                while True:
                    creat=int(input("Create Package"))
                    rtn=int(input("How much Amount You want to return "))
                    td=input("For yearly =y / Monthly =m / Daily =d / Hourly = h ")
                    y="yearly"
                    m="monthly"
                    d="daily"
                    h="hourly"
                    if td=="y":
                        tr=y
                    elif td=="m":
                        tr=m
                    elif td=="d":
                        tr=d
                    elif td=="h":
                        tr=h                  
                    else:
                        print("You Enter wrong value ") 
                    dr=int(input(td ," Time duration in number : "))
                    rtt=int(input("How many amount return percentage after complete Agreement : "))
                    

             

 
                break

            elif a==ua2 and u==ua1:
                print("You Entered successfully ") 
                print("Welcome to Anumarket ") 
                break     
                  
            else:
                print("Sorry please Enter Properly ") 
                break                             
    else:
        print("Sorry your password is incorrect")          
else:
    print("Please enter above 6 digit or above 6 digit password")

