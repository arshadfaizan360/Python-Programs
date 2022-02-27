num = int(input('Enter a number '))

factorial = 1
if num > 1:
    for x in range(2,num+1):
        factorial *= x
print('The factorial of', num, 'is', factorial)