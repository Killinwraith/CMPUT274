"""
--------------------------------------------
Name: Hetang Mehta
SID: 1732484
CCID: hmmehta  
AnonID: xyz
CMPUT 274, Fall 2022

Assessment: WE03 assignment - Word Counter
--------------------------------------------

FREQ TEMPLATE: ADD YOUR INFORMATION TO ABOVE

You must determine how to structure your solution.
Create your functions here and call them from under
if __name__ == "__main__"!
"""

import sys


def make_dict(filename):
    
    file = open(filename, "r")    
    dict = {}

    for line in file:
        line = line.split()
        for word in line:
            if word in dict:
                dict[word] += 1
            else:
                dict[word] = 1 
    
    tw = sum(dict.values())
    fout = open(f"{filename}.out","w")
    [fout.write(f'{x} {y} {round(y/tw,3)}\n') for x,y in sorted(dict.items())]
    fout.close()
    

    


    
if __name__ == "__main__":
    # Any code indented under this line will only be run
    # when the program is called directly from the terminal
    # using "python3 freq.py". This is directly relevant to
    # this exercise, so you should call your code from here.
    def errorcheck():
        if len(sys.argv) < 2:
            print("Too few arguments. Usage: python3 freq.py <input_file_name>")
            sys.exit()
        if len(sys.argv) > 2:
            print("Too many arguments. Usage: python3 freq.py <input_file_name>")
            sys.exit()
    errorcheck()    

    filename = sys.argv[1]
    make_dict(filename)
    pass


"""
--------------------------------------------
Name: Hetang Mehta
SID: 1732484
CCID: hmmehta
AnonID: xyz
CMPUT 274, Fall 2022

Assessment: Weekly Assignment 03 - Word Counter
--------------------------------------------

FREQ TEMPLATE: ADD YOUR INFORMATION TO ABOVE

You must determine how to structure your solution.
Create your functions here and call them from under
if __name__ == "__main__"!
"""

"""

import sys

def make_dict(filename):
    
    #opens the file and reads it as specified in the terminal
    file = open(filename, "r")    
    #creates an empty dictionary
    dict = {}
    
    #this for loop takes every line in the file and splits it into words
    for line in file:
        line = line.split()

        #this for loop takes a single word in the list of lines created above and then adds them to the empty dictionary.
        for word in line:

            #If the word is already present in the dictionary, then it will add 1 to the value of it. 
            if word in dict:
                dict[word] += 1

            #Adds a new key with the word as the key and the value is set to 1. 
            else:
                dict[word] = 1  
    
    #gets the sum of all the words in the text file. 
    totatlword = sum(dict.values())
    #opens a new file, with the same name as the the file that was opened previously but now with a .out behind it.
    #It is also opened as a writeable file. 
    fout = open(f"{filename}.out","w")

    #wirtes in the file opened above...writes every word(key), the amount of times it showed up, and the ratio comapred to the total value.
    [fout.write(f'{x} {y} {round(y/totatlword,3)}\n') for x,y in sorted(dict.items())]
    #closes the file above. 
    fout.close()

    
if __name__ == "__main__":
    # Any code indented under this line will only be run
    # when the program is called directly from the terminal
    # using "python3 freq.py". This is directly relevant to
    # this exercise, so you should call your code from here.
  
    #checks for any error when running the code from terminal. 
    def errorcheck():
        if len(sys.argv) < 2:
            print("Too few arguments. Usage: python3 freq.py <input_file_name>")
            sys.exit()
        if len(sys.argv) > 2:
            print("Too many arguments. Usage: python3 freq.py <input_file_name>")
            sys.exit()
    #runs the error check function.
    errorcheck()    
    
    #sets the filename
    filename = sys.argv[1]

    #calls upon the function that counts and creates a new file. 
    make_dict(filename)
    
    pass

"""