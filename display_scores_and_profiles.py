#Fairus code for displaying the scores and profiles
import csv

#Function to print the profiles and scores
def print_profiles():
    ans = input("What is your name?\n")
    found = False

    with open("Scores.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if ans.upper() in str(row[1]).upper():
                print("Name: ",row[1])
                print("\nEasy reaction test score: ",row[2])
                print("Hard reaction test score: ",row[3])
                print("Number guess score: ",row[4])
                print("\nProfile: ",row[5])
                found = True
                break
    if not found:

        print("This profile doesn't exist please try again\n")  
    
print_profiles()

