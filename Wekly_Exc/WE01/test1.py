text = 'abcdefg'
newt = list(text)
x = 4
text = text[:x] + 'Z' + text[:]
print(text)
print(newt[1])