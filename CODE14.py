#sum of digits of a given number 

x= int(input(" enter the number : "))
f = int(x)
sum=0
while x>0 : 
        t = x % 10
        sum = int(sum + t)
        x = int(x/10)
        
        
print(" sum of digits of "+ str(f) + " is : " + str(sum))      