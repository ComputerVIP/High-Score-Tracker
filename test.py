import csv

with open("Scores.csv", "r") as file:
  reader = csv.reader(file)
  next(file)
  users = []
  for row in reader:
    users.append([row[1], row[2]])
  sorted_users = []
  for user in users:
    sorted_users.append(user[1] + " " + user[0])
  sorted_users = sorted(sorted_users, reverse=True)
  for user in sorted_users:
    name, score = user.split(" ")
    print(f"{score} {name}")