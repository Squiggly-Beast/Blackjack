#Blackjack
#100% bug free

#setup
import random
from random import randint

deck = ["a","a","a","a","1","1","1","1","2","2","2","2","3","3","3","3","4","4","4","4","5","5","5","5","6","6","6","6","7","7","7","7","8","8","8","8","9","9","9","9","10","10","10","10","j","j","j","j","q","q","q","q","k","k","k","k"]

computerhand = []
playerhand = []

#game functions
def draw(player):
       
    number = random.randint(0, len(deck)-1)
    if player == 1:
        playerhand.append(deck[number])
        deck.pop(number)
        
    if player == 0:
        computerhand.append(deck[number])
        deck.pop(number)

    score()
            
def score():

    global playerscore
    global computerscore

    playerscore = 0
    computerscore = 0
    
    for x in range(len(playerhand)):     
        if playerhand[x] is not "a" and  playerhand[x] is not "j" and playerhand[x] is not "q" and playerhand[x] is not "k":
            playerscore = playerscore + int(playerhand[x])
        elif playerhand[x] is not "a":
            playerscore = playerscore + 10
    
    for x in range(len(playerhand)):
        if playerhand[x] is "a":
            if playerscore >= 11:
                playerscore = playerscore + 1
            else:
                playerscore = playerscore + 11
    
    for x in range(len(computerhand)):     
        if computerhand[x] is not "a" and  computerhand[x] is not "j" and computerhand[x] is not "q" and computerhand[x] is not "k":
            computerscore = computerscore + int(computerhand[x])
        elif computerhand[x] is not "a":
            computerscore = computerscore + 10
    
    for x in range(len(computerhand)):
        if computerhand[x] is "a":
            if computerscore > 11:
                computerscore = computerscore + 1
            else:
                computerscore = computerscore + 11


def whowon():

    playerwin = False
    computerwin = False

    print("You had a score of", playerscore)
    print("The computer had a score of", computerscore)

    if playerscore > 21:
        playerwin = False
        print("You went bust")
    else:
        playerwin = True
        
    if computerscore > 21:
        computerwin = False
        print("The computer went bust")
    else:
        computerwin = True

        

    if computerwin is False and playerwin is False:
        print("You both went bust so no one wins")

    elif computerwin is False and playerwin is not False:
        print("You won because the computer went bust")

    elif playerwin is False and computerwin is not False:
        print("The computer won because you went bust")

    elif playerscore > computerscore:
        print("You won because you had a higher score than the computer")

    elif playerscore < computerscore:
        print("The computer won because it had a higher score than you")

    else:
        print("You tied")
    

#deal starter hands

for x in range(2):
    draw(0)
    draw(1)

#player turn
print("Your hand is " + str(playerhand))
print("That makes your score " + str(playerscore))
action = input("Draw or hold: ")
while action != "hold":
    if action == "draw":
        draw(1)

    print("Your hand is " + str(playerhand))
    print("That makes your score " + str(playerscore))
    if playerscore > 21:
        break
    action = input("Draw or hold: ")


#computers turn
while computerscore <= 16:
    draw(0)
    score()

#check who won
whowon()
