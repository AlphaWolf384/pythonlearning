''' Hangman Game v0.1 '''

import time
import random

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

def count_letter(word):
    count = 0
    while count <= len(word):
        count += 1
    return count

#########################################

words = {"apple", "orange", "banana", "wisconsin", "cheese", "pie", "water"}

while True:

    user = raw_input('Play the Hangman game? Y|N ')
    if user == 'Y' or user == 'y':
        num = 0
        secret_word = random.choice(words).lower()
        real_word = count_letter(secret_word)
        guess_word = []
        for letter in secret_word:
            guess_word.append(" - ")
        while True:
            gameBoard(num)
            print(secret_word)
            user_guess = raw_input('Guess a letter: ')
            
    elif user == 'N' or user == 'n':
        print('Aborting now')
        time.sleep(2)
        break
    else:
        print('Press something else? Please Try Again.')
            

    
    


