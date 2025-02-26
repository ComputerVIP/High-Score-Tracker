import csv

ans = input("What is your name?\n")

with open("Scores.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        if ans.upper() in str(row).upper():
            ask = input("What is the password for this profile?\n")
            if ask.upper() in row[0].upper():
                print("Name: ",row[1])
                print("\nHard reaction test score: ",row[2])
                print("Easy reaction test score: ",row[3])
                print("Number guess score: ",row[4])
                print("\nProfile: ",row[5])
        else:
            pass