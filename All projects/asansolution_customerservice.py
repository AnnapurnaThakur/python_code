
def anu():
    
    print(" january ")
    print(" Februry ")
    print(" March ")
    print(" April ")
    print(" May ")
    print(" June ")
    print(" July ")
    print(" Auguest")
    print(" September")
    print(" October ")
    print(" November ")
    print(" December ")


d="salary problem"
e="attendence problem"
f="holiday enquiry"
g="activate/deactivate id"
h="send to other problem messege"
o="exit"

while True:
    
    a=int(input("Press 1 for Login : "))
    if a==1:
        print("You successfully entered ")
        print()
        b=input("Enter Your Name :")
        c=input("Enter your 7 digit Id number :")
        c2="AA" 
        c1=c2+c        # print(c1)
        num=len(c1)
        # print(num)
        if num==9:
            print("Welcome to Asansolution " ,b)
            print("")
            print("How may I help you " + b + "?")
            print("")
            print("select 1 for " , d)
            print("select 2 for " , e)
            print("select 3 for " , f)
            print("select 4 for " , g)
            print("select 5 for " , h)
            print("select 9 for " , o)
            print("")
            x=int(input("Enter your choose : "))
            # print(x)
            if x==1:
                # print("Salary Work in progress " )
                print("you choice " , d)
                anu()
                
                if c2=="AA":
                    print("your salary 50000")
                elif c2 =="BB":
                    print("your salary 30000")
                elif c2=="CC":
                    print("your salary 20000")
                elif c2=="DD":
                    print("Your salary 10000")
                else:
                    print("Your salary 7000")
                break         
            elif x==9:
                break
            elif x==2:
                print(" your choose : " , e)
                anu()
                e1=input("Enter the absent date : " )
                print(e1)
                print("Select 1 for medical / health problem ")
                print("Select 2 for holiday message ")
                print("Select 3 for others problem ")
                print()
                e2=int(input("Which attendence problem you please select right number : "))
                print()
                
                if e2==1:
                    print("please submited doctors prescriptions ")
                elif e2==2:
                    e4=input("Send message : ")
                    
                elif e2==3:
                    print("enter your messenge to send our boss")
                    e5=input(" send message : ")
                print("your message has been send successfully")
                print("your attendence problem fill successfully")
                break
            elif x==3:
                print("you choose " , f)
                print("2020 HOLIDAYS LIST :")
                print("Netaji Subhas Chandra Bose Jayanti	     23 Jan, 2020")
                print("Republic Day	Sun                          26 Jan, 2020")
                print("Basant Panchami	                             29–30 Jan 2020")
                print("Maha Shivratri	                             21 Feb, 2020")
                print("Holi                                   	     9–10 Mar 2020")
                print("Rama Navami	                             2 Apr, 2020")  
            if x==5:
                print("you choose " , h)
                h1=input("enter your message to submit :")
                print("select 1 for send message to boss :" )
                print("select 2 for send message to HR :" )
                print("select 3 for send message to company : ")
                h2=int(input("select your choose : "))
                if h2==1:
                    print("your message send successfully to boss.")
                elif h2==2:
                    print("your message send successfully to HR.") 
                elif h2==3:
                    print("your message send successfully to Company.")
                else:
                    int(input("selet the correct number : "))
                    print("message sent successfully")             
                
            else:
                continue    
            
            print("thank you for using our service . ")       
        
        else:
            print("Sorry you are not allowed in this company. ")
        break
    else:
        print("Please enter the correct number ") 

