'''write a program that  ask the user to input number of seconds and than expresses it in 
terms of many minutes and seconds in containts ?  page no. 35, Q.No. 18
'''
# numseconds=input("Enter number of second : ")
# numseconds_int=int(numseconds)
# numminuts=numseconds_int//60
# remainingseconds=numseconds_int%60
# print('minuts : ', numminuts)
# print('second : ',remainingseconds)



# a=input("Enter second : ")
# b=int(a)
# mint=b//60
# sec=b%60
# h=mint//60
# print(mint , " : Minute ")
# print(sec," : Second " )
# print( h,": hour  ")


# a=input("Enter Minute : " )
# b=int(a)
# c=b*60
# print("second : ", c )
# print("Select 1 for count ")
# d=int(input(" Enter the select number : "))
# if d==1:
#     while d>3:
#         print(d)
import time
a=int(input("Enter your second : "))
for i in range (a,0,-1):
    print(i)
    time.sleep(1)    
print("Go")


