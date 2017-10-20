from random import randint

print("Hello World!", "Welcome to Dice Simulator")
last_number = 0

while True:
        user_input = raw_input('Roll? Y|N: ')
        random_number = randint(0,5) + 1
        if user_input == 'Y' or user_input == 'y':
                print
                print random_number
                print
        else:
                print 'Dice Simulator aborted'
                break
