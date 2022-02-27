howFar = int(input('How far to count? '))
while howFar < 1:
    howFar = int(input('Not a valid number, please try again. '))
for myLoop in range(0,howFar+1):
    if myLoop % 3 == 0 and myLoop % 5 == 0:
        print('FizzBuzz')
    elif myLoop % 3 == 0:
        print('Fizz')
    elif myLoop % 5 == 0:
        print('Buzz')
    else:
        print(myLoop)
