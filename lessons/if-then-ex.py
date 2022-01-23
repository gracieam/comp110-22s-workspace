"""Practicce with if-then-else statements."""

choice: int = int(input("Enter a number: "))

#Implement this logic
# A when < 25
# B when >= 25 and < 50
#C when > 75
#D when >= 50 and <=75

if choice < 25:
    print("A")
else:
    if choice < 50:
        print("B")
    else:
        if choice <= 75:
            print("D")
        else:
            print("C")
