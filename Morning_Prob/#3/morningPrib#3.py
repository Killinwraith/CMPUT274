n,m = map(int, input().split())
enemy_attack = list(map(int,input().split()))
class_attack = list(map(int,input().split()))


collect = [""]*m

for i in range(m):
    k = class_attack[i]
    
    for j in range(n):
        q = enemy_attack[j]
        
        if k > q:
            collect[i] = k
            

for i in range(m):
    if "" in collect:
        collect.remove("")
    else: 
        pass

flag = True
while flag: 
    if collect == []:
        print("-1")
        flag = False
    else:
        jeff = int(max(enemy_attack))
        bob = int(min(collect))
        if bob > jeff: 
            print(bob)
            flag = False
        else:
            collect.remove(bob)
            flag = True
    

    
    
    
    
"""
    
    jeff = max(enemy_attack)
    bob = min(collect)
    if bob > jeff: 
        if bob not in enemy_attack:
            print(bob)
        else:
            print("-1")
    else: 
        print("Fail")
    
"""