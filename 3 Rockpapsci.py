p1 = str(input("Enter choice: "))
p2 = str(input("Enter choice2: "))

if (p1 == "rock" and p2 == "scissor") or (p1 == "scissor" and p2 == "paper"):
    print("p1 wins!!!")
elif (p1 == p2):
    
    print("Tie!!!")
else:
    print("p2 wins!!!")
