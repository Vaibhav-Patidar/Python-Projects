#greeting someone using function
def func1(name="stranger"):
    o = "good day, " + name
    return o
a = func1() #enter someone's name or leave blank for stranger
print(a)