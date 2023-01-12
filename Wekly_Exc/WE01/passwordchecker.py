password = input("Password: ")
def validate(password):
    
    forbchar = [" ","@","#"]
    spechar = list("!-$%&'()*+,./:;<=>?_[]^`{|}~")
    paswmap = [1,1,0,0,0,0]
    #checks if the password is less than 8 cahracters (for invalid)
    if len(password) < 8:
        paswmap[0] = 0
    
    for character in password:
    #check for forbidden character (for invalid)
        if character in forbchar:
            paswmap[1] = 0
        #check for upper case letter (for valid)
        if "A" <= character <= "Z":
            paswmap[2] = 1
        #check for lower case letter (for valid)
        if "a" <= character <= "z":
            paswmap[3] = 1
        #check for decimals (for valid)
        if "0" <= character <= "9":
            paswmap[4] = 1
        #check for special characters (for valid)
        if character in spechar:
            paswmap[5] = 1
    check = [0,0]

    if paswmap[0] + paswmap[1] == 2:
        check[0] = 1

    if paswmap[2] + paswmap[3] + paswmap[4] + paswmap[5] == 4:
        check[1] = 1

    match check:
        case [0,0] | [0,1]:
            return "Invalid"
        case [1,0]:
            return "Insecure"
        case [1,1]:
            return "Secure"



x = validate(password)
print(x)