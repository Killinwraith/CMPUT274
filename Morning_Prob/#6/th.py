n,m,k = list(map(int,input().split()))
scares = []
for i in range(n):
    scares += [list(map(int,input().split()))]
scares = [min(item[i] for item in scares) for i in range(m)]
while sum(scares) > k:
    scares.remove(max(scares))
print(len(scares))