import random
from add_scores import add_score

def guess_1_4():

    game_name = "Guess" # Number Guessing Game

    rpt = input("How many rounds would you like to play?\n")
    try:
        rpt = int(rpt)
    except:
        return ("That is not a valid answer! Make sure it is an integer!")
    score = 0
    rounds = 0
    while rpt > 0:
        gs = int(input("\n\nGuess a number 1-4!\n")) #Get user guess
        cgs = random.randint(1,4) #Computer guesses a number
        if gs == cgs: #If numbers are the same
            score += 1
            rounds += 1
            print("You guessed the computer's number!")
            print(score,"/",rounds)
            rpt -= 1
        else: #If numbers are not the same
            rounds += 1
            print("You did not guess the correct number!")
            print(score,"/",rounds)
            rpt -= 1
    print("\n\n\n",score,"/",rounds)
    print("This is your final score")
    add_score(score, game_name)
    return 