import csv

def print_scores():
    ans = input('''What would you like to do?
    Show highscores for Easy Reaction Test(1)
    Show highscores for Hard Reaction Test(2)
    Show highscores for Number Guess(3)
    ''')
    
    try:
        ans = int(ans)  # Makes sure it can be an integer
    except:
        print("Invalid input!")
        return
    
    if ans < 1 or ans > 3:
        print("Invalid input!")
        return
    
    # Open the CSV file and read it
    with open("Scores.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header line
        users = []
        
        # Collect user data
        for row in reader:
            # Assuming that row[1] is the name and row[ans + 1] is the score for the selected game
            if len(row) > ans + 1:  # Check to ensure the score exists
                users.append([row[1], row[ans + 1]])  # row[1] -> name, row[ans + 1] -> score
        
        # Sort users based on the score in descending order
        sorted_users = sorted(users, key=lambda user: int(user[1]), reverse=True)
        
        # Print the sorted scores
        for user in sorted_users:
            print(f"{user[1]} {user[0]}")