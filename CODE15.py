#rev of number

x = int(input(" enter a number : "))
temp  = int(x)
d = 0 
while x>0:
    a = int(x % 10)
    d = int(d * 10 + a)
    x = int(x/10)
    
    
print(" the reverse of  " + str(temp) + " is " + str(d))    