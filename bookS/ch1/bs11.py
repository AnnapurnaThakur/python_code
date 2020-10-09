aList=[15,6,13,22,52,2]
print("Original list is : ",aList)
n=len(aList)
for i in range(n):
    for j in range(0,n-i-1):
        if aList[j]>aList[j+1]:
            aList[j],aList[j+1]= aList[j],aList[j+1]
print("List after sorting : ", aList)