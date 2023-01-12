n,m,k,minks = tuple(map(int,input().split()))+([],)
for i in range(n): 
    minks += [list(map(int,input().split()))]
minks = [min(item[i] for item in minks) for i in range(m)]
while sum(minks) > k: 
    minks.remove(max(minks))
print(len(minks))




