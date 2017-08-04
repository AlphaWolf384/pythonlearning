''' Dom's Text-Based Adventure '''

from random import randint
import time
import os

''' ========== Name Call ========== '''

penny = False #Story Lore

''' ========== Name Call ========== '''

''' ========== FUNCTIONS ========== '''

def playerSystem(x):
    user_health = 100 #Player's Health
    user_attack = 5 #Player's Attack
    user_defense = 20 #Player's Defense
    user_mode = True #True = Attack mode & False = Defense mode
    user_title = "Peasant"
    print(user_title+" "+x)
    print("Health: " + str(user_health))
    print("Attack: " + str(user_attack))
    print("Defense: " + str(user_defense))
    print("Mode: " + str(user_mode))
    

def startGame():
    print("What's your name?")
    name = raw_input(">")
    
    raw_input("Continue?")
    playerSystem(name)
    print
    print("Once upon a time, a man named Jolken who roamed Earth to desire for power")
    time.sleep(2)
    print("He grew up in a small villages somewhere in mysterious World.")
    time.sleep(2)
    print("One day, Jolken left his home to go fishing and he found penny on the way!")
    time.sleep(2)
    print("Jolken decided to leave it alone.")
    time.sleep(2)
    print("Then there is a old man shouted attention of Jolken.")
    time.sleep(2)
    print("Do you 'respond' or 'ignore'?")
    print("Type any word that are within ' '")
    while True:
        ans1 = raw_input(">")
        if ans1 == "respond" or ans1 == "RESPOND" or ans1 == "Respond":
            route1()
            break
        elif ans1 == "ignore" or ans1 == "IGNORE" or ans1 == "Ignore":
            route2()
            break
        else:
            print("Jolken snoozed...Try Again")

    time.sleep(1)
    route3()
    raw_input("Continue?")
    route4()
    print("I need to stop here because I have life to do")
    raw_input("You have reached the end for now and stay tune for more story")

def route1():
    time.sleep(1)
    print("Jolken walked toward to the old man and see what is going on?")
    time.sleep(2)
    print("The old man mentioned that he was former general of the Fire Nation")
    time.sleep(2)
    print("He urged Jolken that he should pick up penny for a good luck.")
    time.sleep(2)
    print("Jolken thought he was bat-shit crazy so he decided to ignore his advice.")
    time.sleep(2)
    print("The old man warned him that if he doesn't pick that penny up, then bad luck will do to Jolken's favor")
    time.sleep(2)
    print("Do you 'proceed' to pick up penny or Do you 'ignore' to go fishing?")
    while True:
        ans2 = raw_input(">")
        if ans2 == "proceed" or ans2 == "PROCEED" or ans2 == "Proceed":
            print("Jolken picked up penny and put it in his pocket")
            penny = True
            time.sleep(2)
            break
        elif ans2 == "ignore" or ans2 == "IGNORE" or ans2 == "Ignore":
            print("Jolken told him to fuck off and proceed to the lake")
            break
        else:
            print("Jolken snoozed...Try Again")

def route2():
    time.sleep(1)
    print("Jolken decided to be on his way to lake")
    time.sleep(2)
    print("Jolken heard some odd noises behind him so he looked back.")
    time.sleep(2)
    print("Same old man did Bruce Lee Jump flip and stand right front of Jolken.")
    time.sleep(2)
    print("Jolken said, "+"WTF? Who the fuck are you?")
    time.sleep(2)
    print("Hello, My name is Inigo Montoya and you killed my father. Prepare to Die")
    time.sleep(2)
    print("Jolken couldn't believe this shit as he struggled to find his sword somewhere")
    time.sleep(2)
    print("Inigo > Just let me find this sword so I can kill you")
    time.sleep(2)
    print("Jolken was able to sneak away from this lunatic old man")
    time.sleep(2)

def route3():
    print("Few moment later, Jolken arrived at the lake and finds one chair.")
    time.sleep(2)
    print("Jolken decided to sit on that chair and start fishing")
    time.sleep(2)
    print("One hour later")
    time.sleep(5)
    print("Suddenly black charcoals are raining and Jolken was confused.")
    time.sleep(1)
    print("Proceed to 'continue' fishing or 'ask' locals who are fishing nearby?")
    while True:
        ans3 = raw_input(">")
        if ans3 == "continue" or ans3 == "CONTINUE" or ans3 == "Continue":
            time.sleep(1)
            print("Jolken decided to continue fishing, but lake is now black")
            time.sleep(2)
            print("Jolken decided to pack up to go home")
            time.sleep(2)
            break
        elif ans3 == "ask" or ans3 == "ASK" or ans3 == "Ask":
            time.sleep(1)
            print("Jolken proceed to ask the locals about the Black charcoal rain.")
            time.sleep(2)
            print("One of local mentioned that is sign of the Fire Nation prescence.")
            time.sleep(2)
            print("Jolken > Really? Just Really?")
            time.sleep(1)
            print("Jolken decided to leave the lake with his stuff and going back to home.")
            time.sleep(2)
            break
        else:
            print("Jolken snoozed...Try Again")

def route4():
    time.sleep(1)
    print("When Jolken was few miles within of his home, He saw lot of smokes coming out")
    print("in the area where he lived.")
    time.sleep(2)
    print("Jolken moved quickly to hometown")
    time.sleep(5)
    print("It turns out that today is National Marijuara Day so everyone had been smoking.")
    time.sleep(2)
    print("Jolken was like ...okay...")
    time.sleep(2)
    print("Do you decide to 'smoke' some weed or go to 'home'?")
    while True:
        ans4 = raw_input(">")
        if ans4 == "smoke" or ans4 == "SMOKE" or ans4 == "Smoke":
            print("Jolken asked for weed and got one")
            time.sleep(2)
            print("Jolken feels high now")
            time.sleep(2)
            print("Then Jolken sees one guy in Fire Nation suit with mask")
            time.sleep(2)
            print("Jolken doesn't know if it is real or not")
            time.sleep(2)
            print("Do you 'run' away to home or Do you 'walk' up to Fire Nation guy?")
            while True:
                ans5 = raw_input(">")
                if ans5 == "run" or ans5 == "RUN" or ans5 == "Run":
                    print("Jolken successfully ran back to his home.")
                    break
                elif ans5 == "walk" or ans5 == "WALK" or ans5 == "Walk":
                    print("Jolken walked to Fire Nation guy")
                    time.sleep(2)
                    print("Fire Nation Guy > Congulations, you're being invaded!")
                    time.sleep(2)
                    print("Jolken wasn't sure if he was serious so he offered him a hit")
                    time.sleep(2)
                    print("Then Jolken heard big noises like the war is breaking out.")
                    time.sleep(2)
                    print("Jolken > Fuck this shit, I'm going home now.")
                    time.sleep(1)
                    print("Jolken went back to his home.")
                    break
                else:
                    print("Uhhh I don't know but try again")
            break
        elif ans4 == "home" or ans4 == "HOME" or ans4 == "Home":
            print("Jolken walked back to home")
            time.sleep(2)
        else:
            print("Hmm I need to think about the black charcoacl rain back in the lake.")
    

''' ========== FUNCTIONS ========== '''

''' ========== START ========== '''

print("Welcome to Jolken's Story")
print("Version: 0.4")
print

startGame()
time.sleep(5)
print("Play another game? Y|N")
while True:
    print("Play another game? Y|N")
    finalans = raw_input(">")
    if finalans == "Y" or finalans == "y":
        startGame()
    elif finalans == "N" or finalans == "n":
        os.system('cls')
    else:
        print("Try again")
                  

''' ========== START ========== '''
