a=int(input("what is your age ? "))
if a<18:
    print("your age is less than 18 not approval " )
elif a>18 and a<30:
    print("20000-30000 Loan approved")
elif a>30 and a<60:
    print("50000-80000 loan approved")
else:
    print("sorry your age is above 60 Not Approval")
    