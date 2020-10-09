#the list of the product

print("product         price       product code")
print("frock           1000           108")
print("top             600            104")
print("jins            1400           102")
print("saree           2500           109")
print("suit            1500           204")
print("t-shirt          400           100")

#codind for selecting product
a=int(input("enter your product code : "))
b=int(input("how much Quintity do you want :"))

#only code 108
if a==108:
    f=1000
    print("your product is frock" )
    print("price" , f*b)
    if b<5:
        k=f*5/100*b
        print("discount 5%" , k)
        print("you will pay only : " ,b*f-k) 
    elif b>5 and b<20:
        c=f*20/100*b
        print("discount 20%" , c)
        print("you will pay only : " ,b*f-c)
    else :
        e=f*35/100*b 
        print("discount 35%" , e)
        print("you will pay only : " ,b*f-e)

# only code 104
if a==104:
    h=600
    print("your product is top" )
    print("price" , h*b)
    if b<5:
        i=h*5/100*b
        print("discount 5%" , i)
        print("you will pay only : " ,b*h-i) 
    elif b>5 and b<20:
        j=h*20/100*b
        print("discount 20%" , j)
        print("you will pay only : " ,b*h-j)
    else :
        l=h*35/100*b 
        print("discount 35%" , l)
        print("you will pay only : " ,b*h-l)

#only code 109
if a==109:
    h1=2500
    print("your product is saree" )
    print("price" , h1*b)
    if b<5:
        i1=h1*5/100*b
        print("discount 5%" , i1)
        print("you will pay only : " ,b*h1-i1) 
    elif b>5 and b<20:
        j1=h1*20/100*b
        print("discount 20%" , j1)
        print("you will pay only : " ,b*h1-j1)
    else :
        l1=h1*35/100*b 
        print("discount 35%" , l1)
        print("you will pay only : " ,b*h1-l1)

#only code 102
if a==102:
    h2=1400
    print("your product is jins" )
    print("price" , h2*b)
    if b<5:
        i2=h2*5/100*b
        print("discount 5% " , i2)
        print("you will pay only : " ,b*h2-i2) 
    elif b>5 and b<20:
        j2=h2*20/100*b
        print("discount 20%" , j2)
        print("you will pay only : " ,b*h2-j2)
    else :
        p=h2*35/100*b 
        print("discount 35%" , p)
        print("you will pay only : " ,b*h2-p)

#only code 204
if a==204:
    h3=1500
    print("your product is suit" )
    print("price" , h3*b)
    if b<5:
        i3=h3*5/100*b
        print("discount 5%" , i3)
        print("you will pay only : " ,b*h3-i3) 
    elif b>5 and b<20:
        j3=h3*20/100*b
        print("discount 20%" , j3)
        print("you will pay only : " ,b*h3-j3)
    else :
        l3=h3*35/100*b 
        print("discount 35%" , l3)
        print("you will pay only : " ,b*h3-l3)

#only code 100
if a==100:
    h4=1400
    print("your product is T-shirt" )
    print("price" , h4*b)
    if b<5:
        i4=h4*5/100*b
        print("discount 5%" , i4)
        print("you will pay only : " ,b*h4-i4) 
    elif b>5 and b<20:
        j4=h4*20/100*b
        print("discount 20%" , j4)
        print("you will pay only : " ,b*h4-j4)
    else :
        l4=h4*35/100*b 
        print("discount 35%" , l4)
        print("you will pay only : " ,b*h4-l4)
else:
    print("Enter the correct code")
    





