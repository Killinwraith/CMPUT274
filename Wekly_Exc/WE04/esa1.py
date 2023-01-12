import sys


def lower(input):
    lowerList = []

    for i in input:
        lowerWord = i.lower()
        lowerList.append(lowerWord)
    return lowerList


def cleanstuff(lowerList):
    cleanList = []
    appendCharacter = False
    cleanedWord = ""

    for word in lowerList:
        if appendCharacter is True:
            cleanList.append(cleanedWord)
            appendCharacter == False
            # print(cleanList)
            cleanedWord = ""
        for character in word:

            if character.isalnum():
                appendCharacter = True
                cleanedWord = cleanedWord + character

    if appendCharacter:
        cleanList.append(cleanedWord)

        cleanedWord = ""

    return cleanList


def removeNum(cleanList):
    noNumList = []
    appendCharacter = False
    cleanedWord = ""
    counter = 0

    for word in cleanList:
        if word.isdigit():
            noNumList.append(word)
        else:
            '''if appendCharacter == True:
                noNumList.append(cleanedWord)
                appendCharacter == False
                print(noNumList)
                cleanedWord = ""'''
            for character in word:
                counter += 1

                if character.isdigit() == False:
                    appendCharacter = True
                    cleanedWord = cleanedWord + character
                else:
                    doesNothing = "hi"
            if counter == len(word):
                noNumList.append(cleanedWord)
                counter = 0
                cleanedWord = ""
    '''if appendCharacter == True:
        noNumList.append(cleanedWord)
        print(noNumList)
        cleanedWord = ""'''
    # print(noNumList)
    return noNumList


def removeStopWords(noNumList):

    noStopWordsList = []

    for word in noNumList:
        if word not in Stop_Words:
            noStopWordsList.append(word)

    # print(noStopWordsList)
    return noStopWordsList


def finalListPrint(noNumList):
    while "" in noNumList:
        noNumList.remove("")
    print(f"{' '.join(noNumList)}")
    return

# Global List
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


input = input().split()
lowerList = lower(input)
print(lowerList)
cleanList = cleanstuff(lowerList)
print(cleanList)
noNumList = removeNum(cleanList)
print(noNumList)
noStopWords = removeStopWords(noNumList)
print(noStopWords)
finalListPrint(noStopWords)
print(finalListPrint)