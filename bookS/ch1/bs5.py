'''
Q.no. 19 > Write a program the repetedly aks from users some numbers untile string 'done' is typed.
the program should print the sum of all numbers entered ? page no. 35
'''
total=0
s=input('Enter a number or "done": ')
while s!='done':
    num=int(s)
    total=total+num
    s=input('Enter a number or "done": ')
print('the sum of entered number is ', total)