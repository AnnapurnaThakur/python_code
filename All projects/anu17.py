a=int(input("how many members in your Family ?"))
b=int(input("how many menbers want Loan ?"))
for i in range (0,b):
    c=input("name :")
    d=input("address :")
    e=int(input("age :"))
    f=int(input("salary :"))
    if e<18:
        print("your age is less than 18 not approval " )
    elif e>=18 and e<30:
        print("20000-30000 Loan approved")
    elif e>=30 and e<60:
        print("50000-80000 loan approved")
    else:
        print("sorry your age is above 60 Not Approval")
    