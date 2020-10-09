a="Jio"
b="AirTel"
c="idea"
d="BSNL"
e="Vodaphone"

a1="Rs. 399 for 60 days unlimited talk time and 2 GB Net/day"
a2="Rs. 199 for 28 days unlimited talk time and 1.5 GB Net/day"
a3="Rs. 149 for 28 days unlimited talk time and 1 GB Net/day"
a4="Rs. 49  for 38 rs. talktime + 100MB Net"

b1="Rs. 399 for 54 days unlimited talk time and 1.5 GB Net/day"
b2="Rs. 199 for 28 days unlimited talk time and 1 GB Net/day"
b3="Rs. 149 for 28 days unlimited talk time and 500 MB Net/day"
b4="Rs. 49  for 38 rs. talktime + 100MB Net"

c1="Rs. 399 for 60 days unlimited talk time and 2 GB Net/day"
c2="Rs. 199 for 28 days unlimited talk time and 1.5 GB Net/day"
c3="Rs. 149 for 28 days unlimited talk time and 1 GB Net/day"
c4="Rs. 49  for 38 rs. talktime + 100MB Net"

d1="Rs. 399 for 70 days unlimited talk time and 2.5 GB Net/day"
d2="Rs. 199 for 28 days unlimited talk time and 1.5 GB Net/day"
d3="Rs. 169 for 28 days unlimited talk time and 1 GB Net/day"
d4="Rs. 49  for 38 rs. talktime + 100MB Net"

e1="Rs. 399 for 60 days unlimited talk time and 2 GB Net/day"
e2="Rs. 149 for 28 days unlimited talk time and 1 GB Net/day"
e3="Rs. 129 for 28 days unlimited talk time and 500MB Net/day"
e4="Rs. 49  for 38 rs. talktime + 100MB Net"


print("select your phone plan company")

print("Select 1 for  " , a)
print("Select 2 for  " , b)
print("Select 3 for  " , c)
print("Select 4 for  " , d)
print("Select 5 for  " , e)

g=int((input("Select your choose :" )))
if g==1:
    print("Your Choose is Jio")
    print()
    print("The plans are :")
    print(a1)
    print(a2)
    print(a3)
    print(a4)

    x=int(input("Enter Your Plan : "))
    ######JIO#####
    if x==399:
        print("You Selected " , a1)
    elif x==199:
        print("You Selected " , a2)
    elif x==149:
        print("You Selected " , a3)
    elif x==49:
        print("You Selected " , a4)
    else:
        print("There is no such plan Avalable")
        print("Please Enter Currect Plan")
elif g==2:
    print("Your Choose is AirTel")
    print()
    print("The plans are :")
    print(b1)
    print(b2)
    print(b3)
    print(b4)

    ###########AIRTEL#####
    x=int(input("Enter Your Plan : "))

    if x==399:
        print("You Selected " , b1)
    elif x==199:
        print("You Selected " , b2)
    elif x==149:
        print("You Selected " , b3)
    elif x==49:
        print("You Selected " , b4)
    else:
        print("There is no such plan Avalable")
        print("Please Enter Currect Plan")
    
elif g==3:
    print("Your Choose is idea")
    print()
    print("The plans are :")
    print(c1)
    print(c2)
    print(c3)
    print(c4)
    
    ###########IDEA#######

    x=int(input("Enter Your Plan : "))
    if x==399:
        print("You Selected " , c1)
    elif x==199:
        print("You Selected " , c2)
    elif x==149:
        print("You Selected " , c3)
    elif x==49:
        print("You Selected " , c4)
    else:
        print("There is no such plan Avalable")
        print("Please Enter Currect Plan")
elif g==4:
    print("Your Choose is BSNL")
    print()
    print("The plans are :")
    print(d1)
    print(d2)
    print(d3)
    print(d4)
    
    ##########BSNL#####

    x=int(input("Enter Your Plan : "))
    if x==399:
        print("You Selected " , d1)
    elif x==199:
        print("You Selected " , d2)
    elif x==169:
        print("You Selected " , d3)
    elif x==49:
        print("You Selected " , d4)
    else:
        print("There is no such plan Avalable")
        print("Please Enter Currect Plan")

elif g==5:
    print("Your Choose is Vodaphone")
    print()
    print("The plans are :")
    print(e1)
    print(e2)
    print(e3)
    print(e4)
    
    ##########VODAPHONE#########

    x=int(input("Enter Your Plan : "))
    if x==399:
        print("You Selected " , e1)
    elif x==199:
        print("You Selected " , e2)
    elif x==129:
        print("You Selected " , e3)
    elif x==49:
        print("You Selected " , e4)
    else:
        print("There is no such plan Avalable")
        print("Please Enter Currect Plan")
    
    print()
z=int(input("Press 1 to confirm  / press 0 to Cencle : "))
if z==1: 
        print("ok your Recharge Successfull")
elif z==0:
        print("Cencle")

else:
     print("this number is not valied for our service")
print()

print("Thank You For Using Our Service")

