dict = {"Apples":1,"bannas":2,"qwr":3,"g":4,"d":5,"v":5,"sad":6 }
x = str(list(map(str,dict.keys())))
count = 10
[print(f"{x} {y/count}") for x,y in dict.items()]
#print(dict.keys())

"""for key, value in dict.items():
    print(key)
    print(value)
"""