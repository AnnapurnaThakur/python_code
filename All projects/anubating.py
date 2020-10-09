import sys
while True:
    a=int(input("How many amount you want add : "))
    c=0
    while True:
        if a>0:
            b=int(input("how many amount you want invest : "))
            if a>=b:               
                a=a-b
                print("your aval. bal : ",a)                
                c=c+b
                print("total investment :", c)                
            else:
                print("insuficiant balance")
        else:
            d=input("You want to continue : (Y/N)")
            if d=='Y' or d=='y':
                break
            else:
                sys.exit(0)

        
            
            
    


    

    

    
    
    
     
    

    
        
    
