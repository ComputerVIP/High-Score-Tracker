import csv

def print_scores():
  ans = input('''What would you like to do?
  Show highscores for Easy Reaction Test(1)
  Show highscores for Hard Reaction Test(2)
  Show highscores for Number Guess(3)
''')
  try:
    ans = int(ans)
  except:
    print("Invalid input!")
    return
  
  if ans > 3:
    print("Invalid input!")
    return
  elif ans < 1:
    print("Invalid input!")
    return
  
  with open("Scores.csv", "r") as file:
    reader = csv.reader(file)
    next(file)
    users = []
    for row in reader:
      users.append([row[1], row[ans + 1]]) #Look at the score basics to make sure the second number corresponds to the score

    sorted_users = []
    for user in users:
      sorted_users.append(user[1] + " " + user[0])

    sorted_users = sorted(sorted_users, reverse=True)
    
    for user in sorted_users:
      name, score = user.split(" ")
      print(f"{score} {name}")