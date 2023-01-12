n,m = list(map(int,input().split()))
diffrence = int((n*(n+1)/2)-m)
begin = n
for x in range(1,n):
 if (x*(x+1)/2 > diffrence):
  begin = int(x+1)
  break
mapping = (lambda x: x if sum(x) != 1 else [1])((lambda x: [m-sum(x)]+x if m-sum(x) != 0 else x)([*range(begin, n+1)]))
print(f"{len(mapping)}\n{' '.join(map(str,sorted(mapping)))}")