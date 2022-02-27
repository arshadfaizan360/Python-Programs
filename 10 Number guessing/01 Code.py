numberToGuess = int(input('Player One enter your chosen number: '))
while numberToGuess < 1 or numberToGuess > 10:
    print('Not a valid choice, please enter another number: ')
    numberToGuess = int(input())
guess = 0
numberOfGuesses = 0
while guess != numberToGuess and numberOfGuesses < 5:
    guess = int(input('Player Two have a guess: '))
    numberOfGuesses += 1
if guess == numberToGuess:
    print('Player Two wins')
else:
    print('Player One wins')
