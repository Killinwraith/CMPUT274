"""
--------------------------------------------
Name: xyz
SID: xyz
CCID: xyz
AnonID: xyz
CMPUT 274, Fall 2022

Assessment: xyz
--------------------------------------------

FREQ TEMPLATE: ADD YOUR INFORMATION TO ABOVE

You must determine how to structure your solution.
Create your functions here and call them from under
if __name__ == "__main__"!
"""

import sys

    
def stuff(filename):
    dictionary = {}

    fOpen = open(filename, "r")

    for line in fOpen:
        for word in line.split():
            if word not in dictionary:
                dictionary[word] = 0
            dictionary[word] += 1
                
    fOpen.close()

    F_Out_Open = open(f"{filename}.out", "w")

    for wordss, count in sorted(dictionary.items()):       
        F_Out_Open.write(f"{wordss} {str(count)} {str(round(count/sum(dictionary.values()),3))}\n")
    #return(word, counter)



    


if __name__ == "__main__":
    # Any code indented under this line will only be run
    # when the program is called directly from the terminal
    # using "python3 freq.py". This is directly relevant to
    # this exercise, so you should call your code from here.

    fName = sys.argv[1]

    if len(sys.argv) < 2:
        print("Too few arguments. Usage: " + "python3" + sys.argv[0] + sys.argv[1])
        #write the exit thingy here

    elif len(sys.argv) > 2:
        print("Too many arguments. Usage: " + "python3" + sys.argv[0] + sys.argv[1])

    else:
        stuff(fName) 
    
    
