#find the greatest number between 3 numbers
def great(num1,num2,num3):
    if (num1>num2):
        if (num1>num3):
            return num1
        else:
            return num3
    else:
        if(num2>num3):
            return num2
        else:
            return num3
nums = great(7,5,8)
print("the biggest number is " + str(nums))
