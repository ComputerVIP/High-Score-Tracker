
import csv

def print_profiles():
    ans = input("What is your name?\n") #Asks for name
    found = False

    with open("Scores.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if ans.upper() in str(row[1]).upper(): #Prints out their profile and scoring info if the name is the same
                print("Name: ",row[1])
                print("\nEasy reaction test score: ",row[2])
                print("Hard reaction test score: ",row[3])
                print("Number guess score: ",row[4])
                print("\nFavourite genre: ",row[5])
                found = True
                break
    if not found:
        print("This profile doesn't exist please try again\n")   #Error handling