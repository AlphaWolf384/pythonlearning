''' Rock, Paper, Scissors v1.2 '''

from random import randint

print('Press X to stop game')
p_score = 0
c_score = 0
d_score = 0

while True:
    print('Player: ' + str(p_score) + ' & Computer: ' + str(c_score) + ' & Draw: ' + str(d_score))
    player = raw_input('Rock (r), Paper (p), or Scissors (s)? ')
    if player == 'r' or player == 'p' or player == 's':
        chosen = randint(1,3)

        if player == 'r':
            player_sign = 'O'
        elif player == 'p':
            player_sign = '___'
        else:
            player_sign = '>8'

        if chosen == 1:
            computer = 'r'
            computer_sign = 'O'
        elif chosen == 2:
            computer = 'p'
            computer_sign = '___'
        else:
            computer = 's'
            computer_sign = '>8'

        print(player_sign + " vs " + computer_sign)

        if player == computer:
            print('DRAW!')
            d_score += 1
        elif player == 'r' and computer == 's':
            print('PLAYER WIN!')
            p_score += 1
        elif player == 'p' and computer == 'r':
            print('PLAYER WIN!')
            p_score += 1
        elif player == 's' and computer == 'p':
            print('PLAYER WIN!')
            p_score += 1
        else:
            print('COMPUTER WIN!')
            c_score += 1

    elif player == 'x' or player == 'X':
        break
    else:
        print('Please Try again')

    
    
