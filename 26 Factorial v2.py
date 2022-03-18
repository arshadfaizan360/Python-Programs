def factorial(num):
    factorial = 1
    for x in range(1,num+1):
        factorial *= x
    return factorial

print(factorial(int(input('Enter a number and its factorial will be outputted: '))))
