#convert meters into kilometers

x = float(input("enter the distance(meters) : "))

if x > 1000 :
      y = int(x/1000)
else:
    y = 0


x = abs(int(y * 1000 - x))
print("distance  :  " + str(y) + " kilometers " + str(x) + "meters ")  
      
