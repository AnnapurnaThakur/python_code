# code="Annapurna"
# for i in code:
#     print(i,"~", end=" ")

line=input("Enter a line : ")
lowercount=uppercount=0
digitcount=alphacount=0
for a in line:
    if a.islower():
        lowercount+=1
    elif a.isupper():
        uppercount+=1
    elif a.isdigit():
        digitcount+=1
    if a.isalpha():
        alphacount+=1
print("Number of uppercase letter : ", uppercount)
print("Number of lowercase letter : ", lowercount)
print("Number of digits letter    : ", digitcount)
print("Number of alphabets letter : ", alphacount)