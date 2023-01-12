"""
--------------------------------------------
Name: Hetang Mehta
SID: 1732484
CCID: hmmehta
AnonID: xyz
CMPUT 274, Fall 2022

Assessment: WE04 - PREPROCESS
--------------------------------------------

TEMPLATE: ADD YOUR INFORMATION TO ABOVE

You must determine how to structure your solution.
Create your functions here and call them from under
if __name__ == "__main__"!
"""
import sys
spechar = list("!-$%&'()*+,./:;<=>?_[]^`{|}~@#")
numbers = list("0123456789")
Stop_Words = [
    "i", "me", "my", "myself", "we", "our",
    "ours", "ourselves", "you", "your",
    "yours", "yourself", "yourselves", "he",
    "him", "his", "himself", "she", "her",
    "hers", "herself", "it", "its", "itself",
    "they", "them", "their", "theirs",
    "themselves", "what", "which", "who",
    "whom", "this", "that", "these", "those",
    "am", "is", "are", "was", "were", "be",
    "been", "being", "have", "has", "had",
    "having", "do", "does", "did", "doing",
    "a", "an", "the", "and", "but", "if",
    "or", "because", "as", "until", "while",
    "of", "at", "by", "for", "with",
    "about", "against", "between", "into",
    "through", "during", "before", "after",
    "above", "below", "to", "from", "up",
    "down", "in", "out", "on", "off", "over",
    "under", "again", "further", "then",
    "once", "here", "there", "when", "where",
    "why", "how", "all", "any", "both",
    "each", "few", "more", "most", "other",
    "some", "such", "no", "nor", "not",
    "only", "own", "same", "so", "than",
    "too", "very", "s", "t", "can", "will",
    "just", "don", "should", "now"
]


def all(x, condition):
    lowered_word = []

    for word in x:
        t = word.lower()
        lowered_word.append(t)

    def nonalpha(remove_item, use_list):
        cleaned_word_list = []
        for word in use_list:
            word = list(word)
            try:
                val = int(''.join(word))
                if val < 0 :
                    word.remove("-")
                    while '' in word:
                        word.remove('')
                    val = int(''.join(word))
                    cleaned_word_list += [str(val)]
                elif val > 0:
                    cleaned_word_list += [str(val)]
                    
            except BaseException:
                simply = []
                for i in word:
                    if i not in remove_item:
                        simply += [i]
                cleaned_word_list += [(''.join(simply))]
        return cleaned_word_list

    def final(use):
        final_list = []
        for word in use:
            if word not in Stop_Words:
                final_list += [word]
        return final_list

    if condition == "keep-symbols":
        non_Sym = nonalpha(numbers, lowered_word)
        finall = final(non_Sym)
    elif condition == "keep-stops":
        non_Sym = nonalpha(spechar, lowered_word)
        non_Num_Sym = nonalpha(numbers, non_Sym)
        finall = non_Num_Sym
    elif condition == "keep-digits":
        non_Sym = nonalpha(spechar, lowered_word)
        finall = final(non_Sym)
    else:
        non_Sym = nonalpha(spechar, lowered_word)
        non_Num_Sym = nonalpha(numbers, non_Sym)
        finall = final(non_Num_Sym)

    while '' in finall:
        finall.remove('')
    print(f"{' '.join(finall)}")


if __name__ == "__main__":
    # Any code indented under this line will only be run
    # when the program is called directly from the terminal
    # using "python3 preprocess.py". This is directly relevant
    # to this exercise, so you should call your code from here.
    condition = sys.argv[-1]
    x = input().split()
    all(x, condition)
    pass
