import random

check = True
while check:
    pasw = input("Choose from any number great than or equal to 8: ")
    n = int(pasw)
    if n >= 8:
        check = False
    elif n < 8:
        print("Please select a number greater than equal to 8!!")

confirm = "not"
while confirm != "Secure":
    pasw = [""]*n

    l1 = list("abcdefghijklmnopqrstuvwxyz")
    l2 = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    l3 = list("!-$%&'()*+,./:;<=>?_[]^`{|}~")

    for i in range(n):
        x = random.randint(0,3)
        match x:
            case 0:
                x1 = random.randint(0,25)
                pasw[i] = l1[x1]
            case 1:
                x1 = random.randint(0,25)
                pasw[i] = l2[x1]
            case 2:
                x1 = random.randint(0,27)
                pasw[i] = l3[x1]
            case 3:
                x1 = random.randint(0,9)
                pasw[i] = str(x1)
    
        password = "".join(pasw)
        """confirm = validate(password)
        if confirm == "Secure":
            return password"""


print(password)

        
        