name=["anu", "rupam", "ayush", "arohi", "anjali" ,"anita", "sabita", "priya", "suman", "raman", "yash", "souvik" ]
# print(len(name))
print(name)
a=input("Enter a letter : ")
m=len(a)
for i in name:
    if a.lower()==i[:m].lower():
        # print(a.lower())
        # # print(i[:m]).lower())
        # # print(i)
        print(i)