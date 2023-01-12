# PASSWORD VALIDATOR TEMPLATE: REPLACE THIS LINE WITH YOUR FILE HEADER

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
            print("Invalid")
        case [1,0]:
            print("Insecure")
        case [1,1]:
            print("Secure")

def generate(n):
    """ Generates a password of length n which is guaranteed to be Secure according to the given criteria.

    Arguments:
        n (integer): the length of the password to generate, n >= 8.

    Returns:
        secure_password (string): a Secure password of length n. 
    """
    pass

if __name__ == "__main__":
    # Any code indented under this line will only be run
    # when the program is called directly from the terminal
    # using "python3 validator.py". This can be useful for
    # testing your implementations.
    pass

password = input("Password: ")
validate(password)