#odd even

x = int(input(" enter L : "))
y = int(input(" enter H : "))

print(" EVEN : ")
for i in range(x, y+1) :
    if i % 2 ==0 : 
        print(str(i) + " ",end= " ")
        
 
    
print(" \n ODD : ") 
for i in range(x,y+1):
    if i % 2 != 0 : 
       print(str(i) + " ",end = " ")
      