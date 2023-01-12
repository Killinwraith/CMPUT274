m = int(input("sides = "))
width = int(input("width: "))
rolls = [3, 2, 3, 2, 3, 3, 4, 6, 2, 6, 3, 2, 6, 2, 5, 5, 3, 4, 4, 2]

print("Frequency Histogram: {}-sided Die".format(m))
max = rolls.count(1)
for i in range(m):
    if rolls.count(i+1) > max:
    	max = rolls.count(i+1)

for i in range(m):
    j = i+1
    #print(f"%d.{rolls.count(j)}" % j)
    k = round(rolls.count(j)*(width/max))
    #print(k)
    hist = ["-"]*width
    for r in range(k):
        hist[r] = "#"
    
    
    h = "".join(hist)
    #print(h)
    print(f"%d.{h}" % j)    
