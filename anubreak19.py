# for x in range (1,5):
#     for i in range(1,5):
#         if i==3:
#             print("Sorry")
#         print("loop2")
#         break
#     print("loop1")
# print("end")

####2nd example:

for x in range (1,5):
    for i in range(1,5):
        if i==3:
            print("Sorry")
        break
        print("loop2")
    print("loop1")
print("end")


######3rd example:
# for x in range (1,5):
#     for i in range(1,7):
#         if i==3:
#             print("sorry")
#             continue
#         print("loop i= " , i , "and loop i =" ,x)
#     print("loop completed x" , x)
# print("end")