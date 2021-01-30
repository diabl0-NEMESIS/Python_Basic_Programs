#calculator

x = int(input("enter num 1 : "))
y = int(input("enter num 2 : "))

print("1 . ADD\n2 . SUBTRACT\n3 . MULTIPLY\n4 . DIVIDE ")

t = int(input("enter your choice : "))
if t==1 : 
    print("\nresult : " + str(x+y))
elif t==2 : 
     print("\nresult : " + str(x-y))
elif t==3 : 
      print("\nresult : " + str(x*y))
elif t==4 : 
       print("\nresult : " + str(x/y))
else :
       print("\n invalid choice")       
 