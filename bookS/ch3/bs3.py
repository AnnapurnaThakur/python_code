def intrest(principal,time=2,rate=0.10):
    return principal*rate*time

prin= int(input("Enter principal Amount : "))
print("Simpal intrest with default ROI and time value is : ")
si1=intrest(prin)
print("Rs. ", si1)
roi=float(input("Enter rate of Intrest (ROI) : "))
time=int(input("Enter the time year : "))
print("Simpal intrest with your provide  ROI and time value is : ")
si2=intrest(prin,time,roi/100)
print("Rs." , si2)