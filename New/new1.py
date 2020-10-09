'''
write a program to take user name and password from the user and store it into the dictionery and findout the 
choose of 1 for squier dygram to for rectangle dygram  3 for trangle ask the choose from user and also ask the 
lenth and hight if he selected rectrangle or squier and hight and lenth for trangle if for sum how the user forgate 
his password than he need to type help to retrive the user name password ?
'''

l="click 1 for login"
r="click 2 for registration"
f="click 3 for forget password"
print(l)
print(r)
print(f)
a=int(input("Enter your chhoose : "))
###########    Login   ###############

if a==1:
    user=input("Enter your user name : ")
    pas=input("Enter your password")
    print("Enter successfully ")
    

########### New Registration #############
if a==2:
    n=input("Enter your name : ")
    n1=int(input("Enter your moble n no :"))
    n2=input("Enter your user name :")
    n3=input("Enter your password : ")
    print("your registration successfully ")
    

if a==3:
    f1=input("Enter your name : ")
    print(pas)




