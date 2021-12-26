#prints a pattern of star
def star(n):
    for i in range(n):
        print("*"*(n-i))

o = int(input("enter a number"))
o = star(o)
print(o)