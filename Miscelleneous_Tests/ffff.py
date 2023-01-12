n = int(input())


def factorial(number):
    if (number == 0 or number== 1): # base case
        answer = 1 
    else:
        answer = number * factorial(number-1) 
    return answer

nn = factorial(n)

print(nn)