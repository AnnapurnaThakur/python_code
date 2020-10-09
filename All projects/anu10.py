a=input("enter product name :")
print("you enter :", a)
b=1200
print("price" , b)
d=int(input("how many product you want :"))
if d<5:
    e=b*5/100
    print("discount 5%" , e*d)
    print("total amount " , b*d)
    print("total bill" , b*d-e*d)
elif d>=5 and d<10:
    x=b*10/100
    print("disconut 10% " , x*d)
    print("total amount ", b*d)
    print("total bill" , b*d-x*d)
elif d>10 and d<20:
    i=b*25/100
    print("dicoount 25%" ,d*i )
    print("total amount" , b*d)
    print("total bill" , b*d-i*d)
else:
    j=b*50/100
    print("dicount 50%" , d*j )
    print("total amount ", b*d)
    print("total bill", b*d-j*d)    
    



