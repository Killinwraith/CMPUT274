n,m = map(int, input().split())
map = [0]*(n)
for i in range(n):
    map[i] = i+1
lenmap = len(map)

if sum(map) == m:
    print(f"{lenmap}\n{' '.join(str(e) for e in map)}")
    
elif sum(map) > m:
    i = 0
    q = 1
    map.reverse()
    check = True
    k = []
    while sum(k) != m:
        if sum(k) < m:
            k.append(map[i])
        elif sum(k) > m: 
            k.remove(map[i-1])
            k.append(map[i])
        elif sum(k) == m:
            print(f"{len(k)}\n{' '.join(str(e) for e in k)}")
            break
        q += 1
        i += 1

    k.reverse()
    print(f"{len(k)}\n{' '.join(str(e) for e in k)}")
        
            
            
# use the following as inputs and see it cry: 34864 479902984