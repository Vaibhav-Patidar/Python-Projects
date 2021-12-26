# replce a word from a string
def stripp(string,word):
    newStr = string.replace(word, "")
    newStr = newStr.strip()
    return newStr
lol = "   hello how are you   "
output = stripp(lol,"how")
print(output)