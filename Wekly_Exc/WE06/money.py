"""
--------------------------------------------
Name: Hetang Mehta
SID: 1732484
CCID: hmmehta
AnonID: xyz
CMPUT 274, Fall 2022

Assessment: WE04 - PREPROCESS
--------------------------------------------

"""
n = int(input())
w = []
for _ in range(n):
    w += [int(input())]
w.sort()
c = 0
if len(w) <= min(w):
    N = len(w)
else:
    for i, e in enumerate(w):
        if len(w) - e >= i:
            N = e
            k = i
        elif (len(w) - (N + 1) >= k):
            N += 1
            c = 1
    if c:
        N -= 1
print(f"{N}")
