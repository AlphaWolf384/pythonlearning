''' Hangman Game v1.0 '''

import time
from random import choice

def gameBoard(num):
    if num == 0:
        print('   ____')
        print('  |    |')
        print('  |')
        print('  |')
        print('  |')
        print('  |')
        print('----------')
        print
    elif num == 1:
        print('   ____')
        print('  |    |')
        print('  |    O')
        print('  |')
        print('  |')
        print('  |')
        print('----------')
        print
    elif num == 2:
        print('   ____')
        print('  |    |')
        print('  |    O')
        print('  |    |')
        print('  |')
        print('  |')
        print('----------')
        print
    elif num == 3:
        print('   ____')
        print('  |    |')
        print('  |    O')
        print('  |   /|')
        print('  |')
        print('  |')
        print('----------')
        print
    elif num == 4:
        print('   ____')
        print('  |    |')
        print('  |    O')
        print('  |   /|\'')
        print('  |')
        print('  |')
        print('----------')
        print
    elif num == 5:
        print('   ____')
        print('  |    |')
        print('  |    O')
        print('  |   /|\\')
        print('  |   /')
        print('  |')
        print('----------')
        print
    elif num == 6:
        print('   ____')
        print('  |    |')
        print('  |    O')
        print('  |   /|\\')
        print('  |   / \\')
        print('  |')
        print('----------')
        print
        print('GAMEOVER')

#########################################

word = choice(["apple", "orange", "banana", "wisconsin", "cheese", "pie", "water"])

guessed = []
wrong = []
num = 0
turns = 30

print(word)

while turns > 0:
    guess = ""
    gameBoard(num)

    for letter in word:
        if letter in guessed:
            guess = guess + letter
        else:
            guess = guess + "_"

    print(guess)
    print("Turns left: " + str(turns))
    print

    if guess == word:
        print("GAME OVER, YOU WON!")
        time.sleep(5)
        break
        
            
    user = raw_input('Enter the letter: ').lower()

    if user in guessed or user in wrong:
        print('You already guessed this letter ' + user)
    elif user in word:
        print("Correct Letter " + user)
        guessed.append(user)
    else:
        print("Wrong Letter " + user)
        wrong.append(user)
        num += 1
    
    turns -= 1

            
            

    
    


