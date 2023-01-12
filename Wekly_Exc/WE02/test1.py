import random
prob_list = [1/12,1/4,1/3,1/12,1/12,1/6]
#x = input()
n = 20 #int(x)
map =[0]
rolls = []
random.seed((2**32)-1)
for i in range(len(prob_list)):
    sum = map[i] + prob_list[i]
    map.append(sum)
print(map)
for i in range(n):
    rand = random.random() 
    #print(rand)
    for j in range(len(prob_list)):
        if map[j] <= rand and rand < map[j+1]:
            rolls.append(j+1)
            #print(rolls)
print(rolls)
