lenroad,captank,numstation,timeatstation = map(int, input().split())

f = list(map(int,input().split()))

num_refill, curr_refill, limit = 0,0,captank

while limit < lenroad:  
    while curr_refill < numstation-1 and f[curr_refill+1] <= limit:
        curr_refill += 1
        print("curr " + str(curr_refill))
        
    print("---------------------------------------------")
    num_refill += 1 
    print("F: " + str(f[curr_refill]))
    
    limit = f[curr_refill] + captank
    curr_refill += 1
    print("num "+ str(num_refill))
    print("limit "+str(limit))
    print("cur: "+str(curr_refill))
    print("---------------------------------------------")

print(f"{lenroad+(num_refill*timeatstation)}")

        


