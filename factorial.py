def factorial(n):
    one = 1
    two = 2
    three = 3
    result = 1
    for i in range(1,n + 1):
        result *= i
    return result

x = factorial(5)
print(x)
four = 4   
five = 5