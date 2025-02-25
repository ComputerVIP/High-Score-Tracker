#Luke Murdock, Adding Scores
from main import csv

def write(): # 
    with open ("Scores.csv", "w", newline="") as file:
        fieldnames = ["Name","React Score","Box Score","Guess Score","Genre"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(profiles)

def add(score, game_name): # Finds out what to add
    while True:
        found = False
        name = input("What is your username?: ").strip()
        for profile_ind, profile in enumerate(profiles):
            if name == profile["Name"]:
                found = True
                found_ind = profile_ind
                break
        if found == False: # FIX INT INPUT!!!
            choice = input("Couldn't Find Profile\nTry Again(1) Create Profile(2)\n", 2)
            if choice == 1:
                continue
            if choice == 2:
                add_profile(name)
                print("Added Your Profile!")
                found_ind = -1
                break
        elif found == True:
            print("Found Your Profile!")
            break
    if score > profiles[found_ind][f"{game_name} Scores"]:
        profiles[found_ind][f"{game_name} Scores"] = score
        print("Successfully Added Your New Highest Score!")
    elif score <= profiles[found_ind][f"{game_name} Scores"]:
        print("You did not score higher than your highest score, so your score wasn't added")
    write()

def add_profile(name):
    genre = input("What is your favorite game genre?: ").strip()
    new_profile = {
        "Name": name, 
        "React Score": 0,
        "Box Score": 0,
        "Guess Score": 0,
        "Genre": genre
    }
    profiles.append(new_profile)