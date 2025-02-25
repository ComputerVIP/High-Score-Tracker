#This is the main project
import random
import pygame

class Clicked(pygame.sprite.Sprite):
    def __init__(self, color, width, height): #This just makes the sprite, any value specified like rct=Clicked("insert colour here", insert width, insert height)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.randomize_position()

    def randomize_position(self): #This just randomises the sprite's position on screen
        #Adjusted to be -200 so it never goes off screen
        self.rect.x = random.randint(200, 1030)
        self.rect.y = random.randint(200, 470)

from box_react_game import clicky
from react_game import react_test
from number_guess import guess_1_4





def main(repeat):
    ans = input("Which game would you like to play?\n    1 for reaction test box\n    2 for number guess\n    3 for reaction test regular\n    4 for exit\n    Answer here: ")
    if ans == "1":
        clicky(Clicked("white", 200, 200))
    elif ans == "2":
        guess_1_4()
    elif ans == "3":
        react_test()
    else:
        print("Goodbye!")
        repeat = 0
    return repeat
while repeat > 0:
    main(repeat)