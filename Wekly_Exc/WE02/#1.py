# UNFAIR DICE TEMPLATE: REPLACE THIS LINE WITH YOUR FILE HEADER
import random
def biased_rolls(prob_list, s, n): 
    
    length = len(prob_list)
    qw = [0]
    rolls = []
    random.seed(s)
    for i in range(length):
        a = qw[i] + prob_list[i]
        qw.append(a)

    for i in range(n):
        r = random.random()
        for j in range(length):
            if qw[j] <= r and r < qw[j+1]:
                rolls.append(j+1)

    # return the resulting rolls
    return rolls


def draw_histogram(m, rolls, width):
    print("Frequency Histogram: {}-sided Die".format(m))
    max = rolls.count(1)
    for i in range(m):
        if rolls.count(i+1) > max: 
            max = rolls.count(i+1)
    
    for i in range(m):
        j = i+1
        k = round(rolls.count(j)*(width/max))
        hist = ["-"]*width
        for r in range(k):
            hist[r] = "#"
    
        h = "".join(hist)
        print(f"%d. {h}" % j)
    


if __name__ == "__main__":
    # Any code indented under this line will only be run
    # when the program is called directly from the terminal
    # using "python3 unfairDice.py". This can be useful for
    # testing your implementations.
    
    
    
    pass
