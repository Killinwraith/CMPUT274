x = ord('Z')
y = ord('a')
if x < 0:
    pass
print(x)
print(y)
print(ord('z')-ord('a'))
for i in range(8):
    print(str(90+i) + ": " + chr(90+i))


x = input().strip()

numbers = []

for char in x:
    num = ord(char)-97
    if num >= 0:
        numbers.append(num)
    elif num < 0:
        num = abs(num)
        numbers.append(num)
    
print(numbers)

jeff = []

for i in numbers: 
    y = chr(i+97)
    print(y)