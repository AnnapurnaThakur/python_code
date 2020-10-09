'''
write a program to take user name and password from the user and store it into the dictionery and findout the 
choose of 1 for squier dygram to for rectangle dygram  3 for trangle ask the choose from user and also ask the 
lenth and hight if he selected rectrangle or squier and hight and lenth for trangle if for sum how the user forgate 
his password than he need to type help to retrive the user name password ?
'''

# Declearing the first stage

print(" Press 1 for Login ")
print(" Press 2 for Regitration ")
print(" Press 3 for Forget Password ")
a=int(input("Enter your choice : "))

# cearing a dictinary

d1={1:"Login", 2:"Registration", 3:"Forget Password"}

# taking the disition
print("\n")

if a==1:
	print("Welcome to ", d1[1], " System.")

	
	# inclued the data into the Data.txt file.
	path="D:\\PyQt5 Tutorial\\Python\\Data.txt"
	f=open(path, 'r')
	f1=f.read()

	data=""
	list1=[]
	list2=[]
	
	n1=0
	l1=len(f1)
	

	for i in f1:
		if i==" ":
			n1=data
			list1.append(n1)
			data=""
				
		else:
			data=data+i

		
	c1=len(list1)

	for k in range(0,c1):
		if list1[k]==":":
			list2.append(list1[k+1])

	print(list1)
	print()
	print(list2)

	# Login Checking process
	# taking data from user.
	# user=input("Enter the user name : ")
	# password=input("Enter the password : ")




elif a==2:
	print("Welcome to ", d1[2], " System.")
	
	# taking data from user.
	user=input("Enter the user name : ")
	password=input("Enter the password : ")

	# inclued the data into the Data.txt file.
	path="D:\\PyQt5 Tutorial\\Python\\Data.txt"
	f=open(path, 'a')
	f.write("Login \n")
	f.write("User Name : "+user+" Password : "+password+" \n")
	#f.write(user+" "+password+" \n")

elif a==3:
	print("Welcome to ", d1[3], " System.")

else:
	print("What do you think about yourself. please type right number.")