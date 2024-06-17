def factorial(num):
    if num == 0 | num == 1:
        return 1
    else:
        fact = num * factorial(num-1)
        return fact
    

number = 5
result = factorial(number)
print("factorail of given number is:",result)

    
    