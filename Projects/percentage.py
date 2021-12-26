# creating a function to find percentage of 2 people
def percent(marks):
    p = sum(marks)/400*100
    return p

marks = [45,78,86,77]
percentage = percent(marks)

marks2 = [98,69,88,99]
percentage2 = percent(marks2)

print(percentage, percentage2)