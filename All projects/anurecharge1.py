print("welcome to our Company")
print("comapny       code")
print("Jio            102")
print("Airtel         105")
print("Idea           101")
print("BSNL           103")
print("Vodaphone      100")
a=int(input("Which Company should You Recharge enter Recharge Code?"))
print("ok you select jio")
a1=49
print("49")
a2=149
print("149")
a3=199
print("199")
b=int(input("Select your plan ?"))
if a==102:
    if b==49:
        print("ohk you selected " , a1)
        print("38 talk time + 100MB net")
    elif b==149:
        print("You selected " , a2) 
        print("28 Days Unlimitted Talk Time + 1 GB Net")
    elif b==199:
        print("You Selected " , a3)
        print("28 Days Unlimmited Call + 1 GB Net/Day")
    else:
        print("Sorry its not available")
    c=int(input("Press 1 to confirm  / press 0 to Cencle : "))
    if c==1: 
        print("ok your Recharge Successfull")
    elif c==0:
        print("Cencle")
    else:
        print("for Confirm Press 1")
        
