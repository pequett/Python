# rock paper scissors

from random import randint

print("\nReady to play? Remember the console is case sensitive\nKeep it all lowercase and no spaces :)")

player = "Rock"
comp = 0
game_through = True

while game_through:
    print()  # blank space for legibility
    player = input("'rock' ,  'paper' ,  or 'scissors?' : ")
    comp = randint(0, 2)
    print()  # blank space for legibility
    if player == "rock":
        if comp == 0:
            print("tie!")
        elif comp == 1:
            print("paper covers rock, you lose!")
        elif comp == 2:
            print("rock crushes scissors, you win!")
    elif player == "paper":
        if comp == 0:
            print("paper covers rock, you win!")
        elif comp == 1:
            print("tie!")
        elif comp == 2:
            print("scissors cut paper, you lose!")
    elif player == "scissors":
        if comp == 0:
            print("rock crushes scissors, you lose!")
        elif comp == 1:
            print("scissors cut paper, you win!")
        elif comp == 2:
            print("tie!")
    else:
        print("Hm, something went wrong\nMaybe you spelled something incorrectly\nRemember, no capitals or spaces!")

    game = input("\nWould you like to play again?\ntype 'y' if you do and 'n' if you don't : ")

    if game == "n":
        game_through = False
    elif game == "y":
        game_through = True
    else:
        print("Bruh you dont get to play again")
        game_through = False

print("\nEND")
