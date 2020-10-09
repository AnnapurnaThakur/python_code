a=int(input("what is your roll number ?"))
b=int(input("your marks in hindi ?"))
b1=int(input("your marks in english ?"))
b2=int(input("your marks in history ?"))
b3=int(input("your marks in geography ?"))
b4=int(input("your marks in math ?"))
b5=int(input("your marks in science ?"))
c=b+b1+b2+b3+b4+b5
if b==45:
    print("pass")
elif b<45:
    print("fail")
else :
    print("pass")
if b1==45:
    print("pass")
elif b1<45:
    print("fail")
else :
    print("pass")  
if b2==45:
    print("pass")
elif b2<45:
    print("fail")
else :
    print("pass")
if b3==45:
    print("pass")
elif b3<45:
    print("fail")
else :
    print("pass")
if b4==45:
    print("pass")
elif b4<45:
    print("fail")
if b5==45:
    print("pass")
elif b5<45:
    print("fail")
else :
    print("pass")
    print("Total Marks" ,c)
if c >280 and  c<320:
    print("Grade B")
if c<280:
    print("You are FAIL")
    print("total marks :" ,c)
elif c>320 and c<400:
    print("Grade A")
elif c>400 and c<500:
    print("Grade A+")
elif c>550 and c<599:
    print("AA")
elif c>599:
    print("not possible")

