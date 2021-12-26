#find the sum of first n natural numbers
def sum(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return n+sum(n-1)
p = int(input("enter a number -> "))
p = sum(p)
print(p)