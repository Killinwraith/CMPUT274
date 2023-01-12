import random
prob_list = [1/12,1/4,1/3,1/12,1/12,1/6]
length = len(prob_list)
m = [0]
rolls = []
n = int(input("# of Rolls: "))
s = (2**32)-1 #int(input("Seed: "))
random.seed(s)
for i in range(length):
    a = m[i] + prob_list[i]
    m.append(a)

#print(m)

for i in range(n):
    r = random.random()
    for j in range(length):
        if m[j] <= r and r < m[j+1]:
            rolls.append(j+1)
