a=int(input("Enter the 1st no. : "))
b=int(input("Enter the last no. : "))

list1=[]
list2=[]
list3=[]
k=1
for i in range (1,b+1):
    k*=a;   
    list1.append(k)
print(list1)
# for i2 in range (0,len(list1)):
#     l=i2+list1

l=list1[0]+list1[1]+list1[2]

print("Total numbers : " ,l)

for j in range (0,b):
    c=int(input("Enter multiplication value : "))
    list2.append(c)
print(list2)
for s in range (0,len(list1)):
    list3.append(list1[s]*list2[s])
print("Total multiplication value : ",list3)


