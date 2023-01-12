n,m = map(int, input().split())

mapping = []

for x in range(n):
    if m>= sum(mapping)+(n-x):
        mapping += [n-x]
    mapping=sorted(mapping)
print(f"{len(mapping)}\n{' '.join(str(e) for e in mapping)}")