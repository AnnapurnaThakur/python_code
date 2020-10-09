for x in range (1,5):
    for i in range (1,7):
        if i==3:
            print("sorry")
            continue
        print("loop i = " , i , "and loop i=" , x )
    print("loop completed x " , x)
print("end")