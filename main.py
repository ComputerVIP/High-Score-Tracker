#This is the main project
import random
import pygame
import csv

from game_menu import gme_main
from display_scores_and_profiles import print_scores
#from display_profiles import print_profiles


profiles = []
#
with open("Scores.csv", "r") as file:
    reader = csv.reader(file)
    for row_index, row in enumerate(reader):
        if row_index == 0:
            detail_types = row
            continue
        profile = {}
        for detail_index, detail in enumerate(row):
            if detail_index == 1 or detail_index == 2 or detail_index == 3:
                detail = int(detail)
            profile.update({detail_types[detail_index]:detail})
        profiles.append(profile)



def menu(): # Introduces the program and then lets the user choose one of the options
    print("Welcome to this game program, it has two different games and keeps tracks of scores and user profiles")
    while True: # FIX INT INPUT!!!
        choice = int(input("\nGames(1) Scores(2) Profiles(3) Exit(4)\n"))
        if choice == 1:
            gme_main(1)
        elif choice == 2:
            print_scores()
#        elif choice == 3:
#            print_profiles()
        elif choice == 4:
            print("Come Back Soon!")
            break
        else:
            print("Something Broke")
            continue