count = 0
word = 'null'
while 1 == 1:
 word = input("WORD: ")
 if word in ['The','the']:
    count = count + 1
 elif word == 'exit':
    break
 print("Total Word Count: %s" % count)