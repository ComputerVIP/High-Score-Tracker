 #Luke Murdock, Adding Scores
import csv

def read_file(): # Turns a file into a list of dictionary profiles
    profiles = []
    with open("Scores.csv", "r") as file:
        reader = csv.reader(file)
        for row_index, row in enumerate(reader):
            if row_index == 0:
                detail_types = row
                continue
            profile = {}
            for detail_index, detail in enumerate(row):
                if detail_index == 2 or detail_index == 3 or detail_index == 4:
                    detail = int(detail)
                profile.update({detail_types[detail_index]:detail})
            profiles.append(profile)
    return profiles

def write(profiles): # Writes the list of dictonary profiles onto the file
    with open ("Scores.csv", "w", newline="") as file:
        fieldnames = ["Password","Name","React Score","Box Score","Guess Score","Genre"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(profiles)

def add_profile(): # Creates a new profile and puts it onto the list of profiles
    name = input("What is your username for your new profile?:\n").strip()
    password = input("What is your password for your new profile?:\n").strip()
    genre = input("What is your favorite game genre?:\n").strip()
    new_profile = {
        "Password": password,
        "Name": name,
        "React Score": 0,
        "Box Score": 0,
        "Guess Score": 0,
        "Genre": genre }
    return new_profile

def create_profile_choice(): # Lets the user decide if they want to create a new profile or try to find their profile again
    while True:
        try:
            choice = int(input("Couldn't Find Profile\nTry Again(1) Create Profile(2)\n").strip())
        except:
            print("Invalid Input Type")
            continue
        if choice <= 0 or choice > 2:
            print("Not In Range")
            continue
        elif choice > 0 or choice <= 2:
            return choice

def add_score(score, game_name): # Adds the user's new score to their profile if they have its pasword or else it lets them create a new profile
    profiles = read_file()
    while True:
        found = False
        redo = False
        name = input("What is your username? (Type 0 if you don't have one):\n").strip().upper()
        for profile_ind, profile in enumerate(profiles):
            if name == profile["Name"].upper():
                found = True
                found_ind = profile_ind
                print("Found Profile!")
                if score <= profiles[found_ind][f"{game_name} Score"]:
                    break
                password = input("Type Your Password:\n").strip().upper()
                if password == profile["Password"].upper():
                    break
                else:
                    redo = True
                    print("That is not the correct password for this profile. Try Again")
                    break
        if found == False:
            choice = create_profile_choice()
            if choice == 1:
                continue
            elif choice == 2:
                profiles.append(add_profile())
                print("Added Your Profile!")
                found_ind = -1
                break
        elif found == True and redo == False:
            break
        else:
            continue
    if score > profiles[found_ind][f"{game_name} Score"]:
        profiles[found_ind][f"{game_name} Score"] = score
        print("Successfully Added Your New Highest Score!")
    elif score <= profiles[found_ind][f"{game_name} Score"]:
        print("You did not score higher than your highest score, so your score wasn't added\n")
    write(profiles)