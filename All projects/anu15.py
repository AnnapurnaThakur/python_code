#nested for loop
sum=0
for i in range (1,6):
    i2=str(i)
    x1=input("enter the marks of subject number  " + i2 +" : " )
    x=int(x1)
    if x==45:
        print("pass")
    elif x<45:
        print("fail")
    else :
        print("pass")
    sum=sum+x
print("the total  value is :" , sum)
c=sum
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


        
            
        
