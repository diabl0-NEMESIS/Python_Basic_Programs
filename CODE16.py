#HCF

x = int(input("enter first number  : "))
y = int(input("enter second number : "))

if x > y:
        t = y
else:
        t = x
        
for i in range(1, t+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
print(" HCF of " + str(x) + " and " + str(y) + " is : " + str(hcf))            
            