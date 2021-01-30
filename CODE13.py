#distance between 2 points
import math
x1 = float(input("enter x coordinate for p1 : "))
x2 = float(input("enter x coordinate for p2 : "))
y1 = float(input("enter y coordinate for p1 : "))
y2 = float(input("enter y coordinate for p2 : "))

diffx = pow(abs(x2 - x1),2)
diffy = pow(abs(y2 - y1),2)
distance = math.sqrt(diffx + diffy)


print(" (x,y) for p1 : " + "( " + str(x1) + " , " + str(y1)+ " )")

print(" (x,y) for p2 : " + "( " + str(x2) + " , " + str(y2)+ " )")
print(" DISTANCE : " + str(distance))
