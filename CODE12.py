#check whether character is alpha num etc
x= input("enter a character : ")
if x.isalpha() : 
    print("alphabet")
elif x.isnumeric() :
    print("number")
else :
  print("symbol")    
      