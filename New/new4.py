'''
write a program to take user name and password from the user and store it into the dictionery and findout the 
choose of 1 for squier dygram to for rectangle dygram  3 for trangle ask the choose from user and also ask the 
lenth and hight if he selected rectrangle or squier and hight and lenth for trangle if for sum how the user forgate 
his password than he need to type help to retrive the user name password ?
'''

print("click 1 for login : ")
print("click 2 for Registration : ")
print("click 3 for forget password : ")
a=int(input("Enter your choose :"))
click={1:"Login", 2:"Registration", 3:"Forget password"}
path="C:\\Users\\Annapurna Kumari\\Desktop\\python_instruction\\New\\data.txt"

if a==1:
    print("Welcome to ", click[1],"System.")
       
    f=open(path,'r')
    f1=f.read()
    print(f1)
    data=""
    list1=[]
    list2=[]
    n1=0
    l=len(f1)
    for i in f1:
        if i==" ":
            n1=data
            list1.append(n1)
            data=""
            c1=len(list1)
            for k in range(0,c1):
                if list1[k]==":":
                    list2.append(list1[k+1])
    # print(list1)
    # print(list2)
    user=input("Enter the user name : ")
    password=input("Enter the password : ")
    print("* Welcome to the login page * ")
    print("press 1 for squier dygram ")
    print("Press 2 for rectangle dygram ")
    click2={1:"squier dygram", 2:"rectangle dygram"}
    cl=int(input("press your choose : "))
    s=int(input("Enter your colum : "))
    s2=int(input("Enter your Rows :"))
    if cl==1:
        print(click2[1])
        for i in range(1,s2+1):
            for j in range(1,s+1):
                print("*", end=" ")
            print(" ")
    elif cl==2:
        print(click2[2])
        for i2 in range(0,s+1):
            for j2 in range(0,i2):
                print("*", end=" ")
            print(" ")
elif a==2:
    print("Welcome to ", click[2],"System.")
    user=input("Enter the user name : ")
    password=input("Enter the password : ")
    f2=open(path, 'a')
    f2.write("Logon \n")
    f2.write("User name : " + user + "\n" "password : " + password + "\n")
    print("* Your registration successfull * ")
    

elif a==3:
    print("Welcome to ", click[3], " System.")

else:
	print("What do you think about yourself. please type right number.")

    
    