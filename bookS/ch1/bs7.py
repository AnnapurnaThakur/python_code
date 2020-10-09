import time
a=int(input("Enter second : "))
for i in range(a,5,-2):
    # print(i)
    time.sleep(.1)
    print("Hello")

    for j in range(i,5,-2):
        # print(j)
        time.sleep(.1)
    print("Good mrng")
print("")

