import random
from add_scores import add_score
import csv
#Vincent's game


def guess_1_4():
    less = False
    above = False
    game_name = "Guess" # Number Guessing Game
    count = 0

    rpt = input("How many rounds would you like to play?\n") #Asks for round amount
    try:
        rpt = int(rpt)
    except:
        return ("That is not a valid answer! Make sure it is an integer!")
    if rpt < 1:
        print("Not a valid amount of rounds!")
        return
    score = 0
    rounds = 0
    while rpt > 0: #Repeats for how many times you want to play
        try:
            while not (less and above): #Makes sure it is within range
                gs = int(input("\n\nGuess a number 1-4!\n"))
                if gs <= 4:
                    if gs >= 1:
                        above = True
                        less = True
            above = False
            less = False
        except:
            print("Not a valid number!")
            gs = 0
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

    with open("Scores.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header line
        users = []
        
        # Collect user data
        for row in reader:
            # Assuming that row[1] is the name and row[ans + 1] is the score for the selected game
            users.append([row[1], row[4]])  # row[1] -> name, row[ans + 1] -> score
        
        # Sort users based on the score in descending order
        sorted_users = sorted(users, key=lambda user: int(user[1]), reverse=True)
        
        # Print the sorted scores
        for user in sorted_users:
            print(f"{user[1]} {user[0]}")
            count += 1
            if count >10:
                break



    add_score(score, game_name) #Luke's part
    return