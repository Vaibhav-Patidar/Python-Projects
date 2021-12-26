# convert inch to cm
def cm(inch):
    inches = inch*2.54
    return inches
o = int(input("enter the value in inches"))
o = cm(o)
print(o)