from main import csv
def print_scores():
    profiles = []
    #
    with open("Scores.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)