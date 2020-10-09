a=int(input("Press 1 for Login"))

if a==1:
    print()
    
else:
    print("Please Enter 1 for Login")
    int(input("Press 1 for login"))
b=input("Enter Your Name :")
i=input("Enter your 2 digit id number : ")
i2=len(i)
if i2==2:
    print("")

    print("Welcome to you  " + b + " our customer support service ")
    c=int(input("Press 2 For Continue"))
    if c==2:
        print("How Can i help you " ,b)
    else:
        print("Please Enter correct number ")
        int(input("press 2 for continue :"))
    d="salary problem"
    e="attendence problem"
    f="holiday enquiry"
    g="activate/deactivate id"
    h="send to other problem messege"
    o="exit"


    print("select 1 for " , d)
    print("select 2 for " , e)
    print("select 3 for " , f)
    print("select 4 for " , g)
    print("select 5 for " , h)
    print("select 9 for " , o)
    x=int((input("Select your choose :" )))
    if x==1:
        # print("you choice " , d)
        # print(" january ")
        # print(" Februry ")
        # print(" March ")
        # print(" April ")
        # print(" May ")
        # print(" June ")
        # print(" July ")
        # print(" Auguest")
        # print(" September")
        # print(" October ")
        # print(" November ")
        # print(" December ")
        u=input("Enter your group : ")
        u1=u.upper()
        c={"A":30000, "B":22000, "C":15000, "D":10000}
        print("the salary of group ",u, " salary is ",c[u1])
        
    if x==2:
        print("you choose " , e)

        e2=int(input("how many days you absent :"))
        print("which attendence problem you fill :")
        print("select 1 for medical/ health problem ")
        print("select 2 for holiday ")
        print("select 3 for others problems")
        y=int(input("your problem number is : "))
        if y==1:
            
            print("please submited doctors p.....")
            print("your attendence problem fill successfull")
        elif y==2:
            print("your attendence problem fill successfully")
        elif y==3:
            print("enter your messenge to send our boss")
            input(" send message : ")
            print("your message has been send successfully")
        
    if x==3:
        print("you choose " , f)
        print("2020 HOLIDAYS LIST :")
        print("Netaji Subhas Chandra Bose Jayanti	     23 Jan, 2020")
        print("Republic Day	Sun                          26 Jan, 2020")
        print("Basant Panchami	                             29–30 Jan 2020")
        print("Maha Shivratri	                             21 Feb, 2020")
        print("Holi                                   	     9–10 Mar 2020")
        print("Rama Navami	                             2 Apr, 2020")
    if x==4:
        print("you choose " , g)
        print("selct 1 for id actived")
        print("select 2 for id deactivated")
        g2=int(input("select your choose :"))

        if g2==1:
            print("id active requierd submilt successfull our technical support team will contact you soon")
        elif g2==2:
            print("id deactive requierd submilt successfull our technical support team will contact you soon")
    if x==5:
        print("you choose " , h)
        input("enter your message to submit :")
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
        if x==9:
            print("your choose is " , o)
        print("Exit") 
else:
    print("incurrect id number")
    
    print("Thaks for using our customer support ")

    

    

        
        