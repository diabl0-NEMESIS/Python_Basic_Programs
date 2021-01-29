#swap two nums without third var 

x = float(input("enter first number : "))
y = float(input("enter second number : "))

#before
print(8*"---")
print("first  number : " + str(x))
print("second number : "+ str(y))
print(8*"---")
x = x + y
y = x - y
x = x - y

#after
print("first  number : "  + str(x))
print("second number : " + str(y))
