
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors


import random


# function to convert number to name
def number_to_name(num):
    if num == 0:
        return "rock"
    elif num == 1:
        return "Spock"
    elif num == 2:
        return "paper"
    elif num == 3:
        return "lizard"
    elif num == 4:
        return "scissors"
    else:
        return "Error"


# function to convert name to number

def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return "Error"


def rpsls(name):
    player_number = name_to_number(name)
    comp_number = random.randrange(0, 5)

    print("player chooses", name)
    print( "computer chooses", number_to_name(comp_number))

    if (comp_number + 1) % 5 == player_number:
        print("Player wins!")
    elif (comp_number + 2) % 5 == player_number:
        print("Player wins!")
    elif comp_number == player_number:
        print("Player and computer tie!")
    else:
        print("Computer wins!")
    print("")


player_guess = input('Enter your choice.. Options:\nrock(0), Spock(1), paper(2), lizard(3), scissors(4)')

rpsls(str(player_guess))





