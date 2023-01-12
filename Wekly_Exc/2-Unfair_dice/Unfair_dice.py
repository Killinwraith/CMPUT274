# UNFAIR DICE TEMPLATE: REPLACE THIS LINE WITH YOUR FILE HEADER
"""
Name : Hetang Mehta
SID : 1732484
CCID : hmmehta
AnonID : 1000339978
CMPUT 274 , Fall 2022


Weekly assignment #2
"""

import random
def biased_rolls(prob_list, s, n): 
    
    #This function returns a list of rolls with biased probabillities 
    
    length = len(prob_list)
    qw = [0]
    rolls = []
    random.seed(s)
    
    #This for loop creates the list qw, whose list values go from 0 to 1 using the probabilities as increments. 
    for i in range(length):
        a = qw[i] + prob_list[i]
        qw.append(a)
    
    #This for loop uses the seed value to creat a set of random numbers(0,1) 
    for i in range(n):
        r = random.random()
        
        #This for loop uses the set of random numbers between (0,1) to choose the correct face value
        for j in range(length):
            if qw[j] <= r and r < qw[j+1]:
                rolls.append(j+1)

    # return the resulting rolls
    return rolls


def draw_histogram(m, rolls, width):
    
    #This function draws a histogram for the rolls by printing it out

    print("Frequency Histogram: {}-sided Die".format(m))
    max = rolls.count(1)

    #This for loop checks for maximum face value of the die. 
    for i in range(m):
        if rolls.count(i+1) > max: 
            max = rolls.count(i+1)
    
    #This for loop scales and prints the graph of each face. 
    for i in range(m):
        j = i+1
        k = round(rolls.count(j)*(width/max))
        hist = ["-"]*width

        #this for loop marks the number of times the face value shows up
        for r in range(k): 
            hist[r] = "#"
    
        h = "".join(hist)
        print(f"%d.{h}" % j)
    


if __name__ == "__main__":
    # Any code indented under this line will only be run
    # when the program is called directly from the terminal
    # using "python3 unfairDice.py". This can be useful for
    # testing your implementations.
    pass