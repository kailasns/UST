p1 = input("Enter email: ")
countr = 0
for i in p1:
      if ((i =="@") or (i == ".")):
        countr = countr + 1
if (countr != 2) or  (p1[0] == "@"):
    print ("enter a valid email")
else:
    print("Valid email")
    
