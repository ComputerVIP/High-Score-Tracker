#This is the main project
from game_menu import name_game
from sort_scores import print_scores
from display_scores_and_profiles import print_profiles

def menu(repeat):
    print("\nWelcome to this game program! It has two different games and keeps track of scores and user profiles.")
    try:
        choice = int(input('''What would you like to do?
    Play games(1)
    Show highscores(2)
    Show your profile(3)
    Exit(4)
'''))
    except ValueError:
        print("Invalid Input Type")
        return repeat

    if choice == 1:
        result = name_game(repeat)
        if result != 0:  
            repeat = result
    elif choice == 2:
        print_scores()
    elif choice == 3:
        print_profiles()
    elif choice == 4:
        print("Come Back Soon!")
        return 0
    else:
        print("Not In Range")

    return repeat

if __name__ == "__main__":
    repeat = 1
    while repeat > 0:
        repeat = menu(repeat)