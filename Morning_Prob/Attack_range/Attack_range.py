# your solution goes here

n,m = map(int, input().split())
enemy_attack = list(map(int,input().split()))
class_attack = list(map(int,input().split()))

#Creates an empty list which stores the ranges of the class attack that are greater than the enemy attack. 
collect = [""]*m

#For loop compares all the class attack to the enemy attacks and stores all the class attacks
#that are greater than the enemy attack in collect. 
for i in range(m):
    k = class_attack[i]
    for j in range(n):
        q = enemy_attack[j]
        if k > q:
            collect[i] = k

#this for loop removes all the empty space that are in the collect list. 
for i in range(m):
    if "" in collect:
        collect.remove("")
    else:
        pass

#This while loop checks which attack is the most suitable attack
#by comparing the maximum range value of the Enemy attack with the minimum range value of collect. 
flag = True
while flag:
    if collect == []:
        print("-1")
        flag = False
    else:
        max_ene = int(max(enemy_attack))
        min_col = int(min(collect))

        #This if loop checks if the minimum value of the 
        #acceptable ranges of the class attack are greater than the maximum range of the Enemy attack.
        #If it is then it will print that value, but if it smaller then it will remove that minimum value and re-test.
        if min_col > max_ene:
            print(min_col)
            flag = False
        else:
            collect.remove(min_col)
            flag = True