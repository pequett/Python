from random import randint

redo = True

replay = "no"

while redo is True:
    goal = randint(1, 10)
    guess = input("Guess a number from 1-10 : ")
    if guess == goal:
        print("Correct!")
        replay = input("Would you like to play again? (type 'yes')  ")
        if replay == "yes":
            redo = True
        else:
            redo = False
    else:
        print("You lost...\nThe number was :", goal)
        replay = input("Would you like to play again? (type 'yes')  ")
        if replay == "yes":
            redo = True
        else:
            redo = False
print("Done")
