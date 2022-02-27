### Heads or Tails

### Author: Faizan Arshad 12D
### Date Created: 14/09/21
### Date Edited: 16/09/21

### To-Do:
# Finish the external file saving - Done ###
# Comment Code - Done ###
# Create validation library - Incomplete

#Importing modules
import random
import datetime
import time

#Initialises the game
def start():
    global heads, tails, name, wins, games
    heads, tails, wins, games = 0,0,0,0
    name = input('What is your name? (or type quit to quit) ')
    if name != 'quit':

        end = False
        while end != True:
            games += 1
            if play() == True:
                wins += 1
            end = playAgain()

        print()
        print('You scored ' + str(wins) + ' wins from a total of ' + str(games) + ' coin flips')
        print()
        print('-------------------------------------------------------------------------')
        print()
        start()


#Flips coin and decides whether user has won or lost
def play():
    print()

    choice = guess()

    print(name + ', you guessed ' + choice)    

    coin = random.choice(['heads', 'heads','tails', 'tails', 'tails', 'tails'])

    print('The coin flipped a ' + coin)

    if choice == coin:
       print('Well done ' + name + ', you correctly guessed ' + coin)
       return True
    else:
        return False

#Does the user want to play again?
def playAgain():
    print()
    choice = input('If you want to quit, enter end. If not, enter anything else ')
    if choice == 'end':
        save()
        return True
    else:
        return False

#Allows user to inputs guess and validates it
def guess():
    while True:
        guess = input('Heads or tails? ')

        global heads, tails
        if guess != 'heads' and guess != 'tails':
            print('That is not a valid choice, make sure you use all lower case letters')
        if guess == 'heads':
            heads += 1
            return guess
        else:
            tails += 1
            return guess

#Saves game data to an external .txt file
def save():
    file = open('stats.txt', 'a')
    file.write('Name: ' + name + '\n')
    file.write('Heads: ' + str(heads) + '\n')
    file.write('Tails: ' + str(tails) + '\n')
    file.write('Date: ' + str(datetime.date.today()) + '\n')
    file.write('Time: ' + str(time.strftime("%H:%M:%S", time.localtime())) + '\n')
    file.write('Games: ' + str(games) + '\n')
    file.write('Wins: ' + str(wins) + '\n')
    file.write('Losses: ' + str(games-wins) + '\n')
    file.write('\n')
    file.close()

start()
