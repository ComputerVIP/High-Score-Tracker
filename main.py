#This is the main project
import random
import pygame
import csv
from game_menu import gme_main
from display_scores import print_scores
#from display_profiles import print_profiles

def menu(): # Introduces the program and then lets the user choose one of the options
    print("Welcome to this game program, it has two different games and keeps tracks of scores and user profiles")
    while True:
        try:
            choice = int(input("\nGames(1) Scores(2) Profiles(3) Exit(4)\n"))
        except:
            print("Invlaid Input Type")
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
           print("Not In Range")
           continue

menu()