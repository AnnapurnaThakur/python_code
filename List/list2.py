##FOR SEARCH 1ST LETER

name=["anu", "rupam", "ayush", "arohi", "anjali" ,"anita", "sabita", "priya", "suman", "raman", "yash", "souvik" ]
print(name)
a=input("Enter your leter : ")
m=len(a)
for i in name:
    if a==i[:m]:
        print(i)
