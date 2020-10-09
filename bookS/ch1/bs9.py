import time
a=int(input("Enter the intervel time : "))
list1=["Hello", "Sir", "I" , "Am", "Anu", "Welcome", "To", "Asansolution", "Thank You", "For Visiting Us"]
l=len(list1)
a2=a/(l+1)
# print(a2)
for i in range (0,l):
    time.sleep(a2)
    l2=list1[i]
    print(l2)
print("Visit Again.....***")