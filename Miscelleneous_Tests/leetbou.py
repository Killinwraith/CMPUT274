s = input()
t = input()

s = list(s)
t = list(t)
        
lenx = len(s)
        
map = [0]*lenx
maptest = [1]*lenx
        
for i in range(lenx):
    if s[i] in t:
        map[i] = 1
    else:
        map[i] = 0
                
if map == maptest:
    print("True")
else:
    print("False")