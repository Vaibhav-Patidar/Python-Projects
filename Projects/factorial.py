#printing factorial using normal method
n = 4
product = 1
for i in range (n):
    product = product*(i+1)

#printing facotrial using function
def factorial_iter(n):
    product = 1
    for i in range (n):
        product = product*(i+1)
    return product

#printing factorial using recursion
def fun(lol):
    if lol == 1 or lol == 0:
        lol = 1
        return lol
    else:
        lol*fun(lol-1)
        return lol

o = int(input("enter a number"))
o = fun(o)
print(o)