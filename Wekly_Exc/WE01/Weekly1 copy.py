# PASSWORD VALIDATOR TEMPLATE: REPLACE THIS LINE WITH YOUR FILE HEADER
import random

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

    #This if statement and match case is created to recognize if the password typed was a Invalid, Insecure, or a Secure password. 
    if paswmap[0] + paswmap[1] == 2:
        check[0] = 1

    if paswmap[2] + paswmap[3] + paswmap[4] + paswmap[5] == 4:
        check[1] = 1

    if check == [0,0]:
        return "Invalid"
    elif check == [0,1]:
        return "Invalid"
    elif check == [1,0]:
        return "Insecure"
    elif check == [1,1]:
        return "Secure"



def generate(n):
    confirm = "not"
     
    #This while loop ensures the password genterated is always Secure
    while confirm != "Secure":
        pasw = [""]*n

        #Character types
        l1 = list("abcdefghijklmnopqrstuvwxyz")
        l2 = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        l3 = list("!-$%&'()*+,./:;<=>?_[]^`{|}~")

        #This for loop creates the secure password, with the length specified by the user. 
        for i in range(n):
            x = random.randint(0,3)
            #chooses a random ascii_lowercase
            if x == 0:
                x1 = random.randint(0,25)
                pasw[i] = l1[x1]
            #chooses a random ascii_uppercase
            elif x == 1:
                x1 = random.randint(0,25)
                pasw[i] = l2[x1]
            #chooses a random special chracter
            elif x == 2:
                x1 = random.randint(0,27)
                pasw[i] = l3[x1]
            #chooses a random integer between 0 to 9
            elif x == 3:
                x1 = random.randint(0,9)
                pasw[i] = str(x1)
                    
        #Checks if the generated password is Secure by running it through the Validator
        password = "".join(pasw)
        confirm = validate(password)
    if confirm == "Secure":
        return "Password is: " + password

#main = input("Do you want a password generated (Y/N): ")

if __name__ == "__main__":
    """ if main in ["Y", "y"]:
        check = True
        while check:
            pasw = input("Choose from any number great than or equal to 8 for the lenght of your password: ")
            n = int(pasw)
            if n >= 8:
                check = False
            elif n < 8:
                print("Please enter a number great than or equal to 8!!!")
        password = generate(n)
        print(password)
    else:
        password = input("Password: ")
        x = validate(password)
        print(x) """
pass
    

