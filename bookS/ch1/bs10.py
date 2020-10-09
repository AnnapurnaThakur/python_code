#Quiz
import time
list1=["1. Which state launch a project that aims to provide free internet access to the poor in the State ? ", "2. Name the first cricketer to score 1000 runs in an innings in any competitive match? ","3. According to international standard, what is the distance of marathon race?","4. The super computer ‘PARAM’ was developed by", "5. Who is said to be the father of Indian Space Programme? "]

l=len(list1)
# print(l)

d1=["1:Sikkim 2:Kerala 3:Karnataka 4:Assam", "1: Prithvi Shaw, 2: Pranav Dhanawade, 3: Virat Kohli 4: Shikhar Dhawan", "1:26 miles 385 yards 2: 26 miles 3: 36 miles 500 yards 4: 22 miles", " 1: TATA 2: IIT-Kharagpur 3: IIT-Kanpur 4: C-DAC", " 1: Abdul Kalam 2: Rakesh Sharma 3: Vikram Sarabhai 4:  Homi Bhabha"]

d=len(d1)
# ansr=[]
d2=[2,2,1,4,3]

for i in range(0,l): 
    
    l2=list1[i]    
    print(l2)
    # print(d) 
    time.sleep(1)  
    print()
    print("Your options are : " , d1[i])
    
    q=int(input("Enter your choose : "))
    time.sleep(2)  
    print()
    if q==d2[i]:
        print("Right")
    else:
        print("Wrong")
    time.sleep(2)  
    print("Next : ")

# score=d2[i]*1
# print("Score : ", score)



    
    