#prime number 

x = int(input(" enter the number : "))
f=0
for i in range(2,x):
    if x % i == 0:
        print(" not prime ")
        f=1
        break
if f==0:
    print(" prime ")
    
    