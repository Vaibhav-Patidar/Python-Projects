def listflatten(inputList):
    for i in inputList:
        if type(i) == int:
            outputlist.append(i)
        elif type(i) == list:
            listflatten(i)
    return outputlist
outputlist = []
toflatten = [1,7,[5,37,[[[[[5,[[[8,[[[25]]]]]]]]]]],29],9]
o = listflatten(toflatten)
list.sort(o)
print(o)