n = int(input())
k = list(map(int, input().split()))


maxk = max(k)
#print("this is max: " + str(maxk))
indexk = k.index(maxk)

upind = indexk + 1
lowind = indexk - n

#print(upind)
#print(lowind)

jeff = k[:upind:]

#print(jeff)
#print("This is the len of jeff: " + str(len(jeff)))
minj = min(jeff)
#print("this is min: " + str(minj))

profit = maxk - minj

if profit > 0:
    print(profit)
elif profit <= 0:
    print("0")