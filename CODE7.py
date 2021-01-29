#avg marks of 5 subs

sum =0

for i in range (5) : 
    x = int(input(" enter marks : "))
    
    sum = sum + x

avg = sum/500
per = avg * 100

print("average : " + str(avg))
print("percentage : " + str(per))    