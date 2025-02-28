
import csv

def print_profiles():
    while True:
        ans = input("What is your name?\n")

        with open("Scores.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if ans.upper() in str(row[1]).upper():
                    print("Name: ",row[1])
                    print("\nHard reaction test score: ",row[2])
                    print("Easy reaction test score: ",row[3])
                    print("Number guess score: ",row[4])
                    print("\nProfile: ",row[5])
                    found = True
                    break
        if not found:
            print("This profile doesn't exist please try again\n")  

print_profiles()
