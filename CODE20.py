#perfect number

x = int(input(" enter the number : "))
sum=0
for i in range(1,x):
    if x % i ==0 : 
        sum = int(sum + i)

if sum == x:
 print(str(x) + " is a perfect number " )
else :
 print(" not a perfect number ")        