x = input().split()
y=[]
for word in x:
    t = word.lower()
    y.append(t)
spechar = list("!-$%&'()*+,./:;<=>?_[]^`{|}~@#")

dahmer =[]


for word in y:
    word = list(word)
    for i in range(len(word)):
        lol = word[i]
        if lol in spechar:
            print("found you " + i)
            word.remove(i)
    dahmer.append(''.join(word))

for word in dahmer:
    for i in word:
        try:
        # Convert it into integer
            val = int(i)
            
        except: 
            pass

print(f"{' '.join(dahmer)}")