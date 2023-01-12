lenroad,captank,numstation,timeatstation = map(int, input().split())

f = list(map(int,input().split())) + [lenroad]

num_r = 0
curr_r = 0
limit = captank

while limit < lenroad:  
    while f[curr_r+1] <= limit:
        curr_r += 1
            
    num_r += 1 
    limit = f[curr_r] + captank
    curr_r += 1

print(f"{lenroad+(num_r*timeatstation)}")