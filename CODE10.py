#convert to lowercase

x = input("enter a character : ")

if x.islower() :
    print("lowercase already")
    
else : 
   x = x.lower()
   print("converted to lowercase : " + x)    