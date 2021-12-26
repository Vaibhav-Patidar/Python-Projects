import random

def game(a,b):
    if a == b:
        return None
    elif a == "r":
        if b == "p":
            return True
        elif b == "s":
            return False
    elif a == "p":
        if b == "s":
            return True
        elif b == "r":
            return False


print("Computer's turn: Rock(r) Paper(p) Scissors(s)")
randNo = random.randint(1,3)
if randNo == 1:
    a = "r"
elif randNo == 2:
    a = "p"
elif randNo == 3:
    a = "s"
b = input("Your turn: Rock(r) Paper(p) Scissors(s) ")

result = game(a,b)
print(f"Computer Choose: {a}")
print(f"You Choose: {b}")

if result == None:
    print("The game is a tie")
elif result:
    print("You Win!")
else:
    print("You Lose")