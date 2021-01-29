#find area of triangle

import math


#sides of the triangle
a = float(input("enter 1st side : "))
b = float(input("enter 2nd side : "))
c = float(input("enter 3rd side : "))

s = float((a + b + c)/2)

#calculated area using heron's formula

area = math.sqrt(float(s * (s-a) * (s-b) * (s-c)))

print("area of triangle : " + str(area))

