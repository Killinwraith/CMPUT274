n = int(input())
string1 = input()

sharps = string1.count("#")
flats = string1.count("b")

if sharps > flats:
    x = sharps-flats
    print("#"*x)
elif flats > sharps:
    x = flats-sharps
    print("b"*x)
elif sharps == flats:
    x = 0
    print("0")


