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

l=sum(list1)

print("Total numbers : ***" ,l)

for j in range (0,b):
    c=int(input("Enter multiply value : "))
    list2.append(c)
l2=sum(list2)
print("total multply value is : ***", l2)
print(list2)
for s in range (0,len(list1)):
    list3.append(list1[s]*list2[s])
print("Total multiplication value : ",list3)
l3=sum(list3)
print("Total multiply value : ***", l3)

