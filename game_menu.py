import pygame
import random

repeat = 1

class Clicked(pygame.sprite.Sprite):
    def __init__(self, color, width, height): #This just makes the sprite, any value specified like rct=Clicked("insert colour here", insert width, insert height)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.randomize_position()

    def randomize_position(self): #This just randomises the sprite's position on screen
        #Adjusted to be -+250 so it never goes off screen
        self.rect.x = random.randint(250, 980)
        self.rect.y = random.randint(250, 420)

from box_react_game import clicky
from react_game import react_test
from number_guess import guess_1_4 as guess
#Hi




def name_game(repeat):
    try:
        ans = int(input('''
Which game would you like to play?
    Reaction test hard(1)
    Reaction test easy(2)
    Number guess(3)
    Exit(4)
'''))
    except TypeError:
        print("Invalid input!")
        repeat = 0
        ans = "Error"
    if ans == 1:
        clicky(Clicked("white", 250, 250)) #Makes the sprite
    elif ans == 2:
        react_test()
    elif ans == 3:
        guess()
    else:
        print("Goodbye!")
        repeat = 0
    return repeat

if __name__ == "__main__":
    repeat = 1
    while repeat > 0:
        repeat = name_game(repeat) #Runs the main function