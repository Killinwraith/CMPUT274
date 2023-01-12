n = int(input())
k = list(map(int, input().split()))


mink = min(k)
#print("this is min: " + str(mink))
indexk = k.index(mink)
upind = indexk + n +1
jeff = k[indexk:upind:]

#print(jeff)
print("This is the len of jeff: " + str(len(jeff)))
maxj = max(jeff)
#print("this is max: " + str(maxj))

profit = maxj-mink

if profit > 0:
    print(profit)
elif profit <= 0:
    print("0")
