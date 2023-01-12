"""
Name: Hetang Mehta
SID: 1732484
CCID: hmmehta
AnonID: 1000339978
CMPUT 274, Fall 2022

Assessment: Morning Problem: Market_madeness
"""

_ = int(input())
k = list(map(int, input().split()))

profit = 0
minv = k[0]

for i in range(len(k)):

    if k[i] < minv:
        minv = k[i]
    else:
        bigboi = k[i] - minv
        if bigboi > profit:
            profit = bigboi

print(profit)
