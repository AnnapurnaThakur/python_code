import time
a=int(input("Enter the total time  : "))
b=int(input("Enter intervel time : "))
c=int(input("Decrese time : "))
for i in range(a,b,-c):
    # print(i)
    time.sleep(1)
    print("Hello", end=" ")

    for j in range(i,-c):
        # print(j)
        time.sleep(1)
    print("Good mrng")
print("")

