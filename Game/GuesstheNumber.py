from random import randint
import time

turn = 1
selected_num = randint(0,100)

print("Welcome to Guess the NUmber v0.5")
print("You will guess the number that computer came with and can you guess it by seven turns?")
print("The number will be between 0- 100")
option = raw_input("Option to show number? Y|Any Key ")

print
print

while True:
    if option == "Y" or option == "y":
        print(selected_num)
    print("Turn: " + str(turn))
    user_guess = raw_input("Guess the Number: ")
    turn += 1

    if int(user_guess) == int(selected_num):
        print("You guessed the Number!")
        user_game = raw_input("Continue next number? Y|N ")
        if user_game == "Y" or user_game == "y":
            turn = 1
            selected_num = randint(0,100)
        elif user_game == "N" or user_game == "n":
            print("Aborting")
            time.sleep(2)
            break
        else:
            print("Please try again")
    else:
        if turn == 8:
            print("It was " + str(selected_num))
            user_shit = raw_input("You didn't guess the number in time! Continue next number? Y|N")
            if user_shit == "Y" or user_shit == "y":
                turn = 1
                selected_num = randint(0,100)
            elif user_shit == "N" or user_shit == "n":
                print("Aborting")
                time.sleep(2)
                break
            else:
                print("Please try again")
        else:
            print("You didn't guessed right number :(")
            difference = int(selected_num) - int(user_guess)
            if difference < 0:
                if difference <= -1 and difference >= -3:
                    print("Warmer lower!!")
                elif difference <= -4 and difference >= -7:
                    print("Warm Lower!")
                else:
                    print("Too low")
            elif difference > 0:
                if difference >=1 and difference <= 3:
                    print("Warmmer high!!")
                elif difference >= 4 and difference <= 7:
                    print("Warmmer high!!")
                else:
                    print("Too high")


