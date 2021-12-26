#print multiplication table of a number
def multiply(n):
    if n == False:
        for i in range(10):
            print(1*(i+1))
    else:
        for i in range(10):
            print(n*(i+1))

number = int(input("enter a number "))
table = multiply(5)
print(table)