#This is the main project
import random
import pygame
import cProfile

repeat = 1

def prfile():
    pass
def scores():
    pass

#Vincent's game with Luke's profiling at the end
def react_test(repeat):

    #Variables to keep track of the score, and amount of rounds
    score = 0
    rounds = 0

    # Initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True

    click_detected = False
    waiting_for_click = False
    start_time = None  
    reaction_start_time = None  # Timer for reaction delay

    while running:
        screen.fill("black")  # Clear the screen

        # Handle Pygame events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and waiting_for_click:
                click_detected = True
                print("Mouse clicked!")

        # If waiting for the delay before reaction starts
        if reaction_start_time is not None:
            if pygame.time.get_ticks() >= reaction_start_time:  # Check if delay is over
                screen.fill("white") #Screen goes white
                pygame.display.flip()
                start_time = pygame.time.get_ticks()  # Starts timer
                reaction_start_time = None  # Stop timer to wait random amount of time
                waiting_for_click = True  # Wait for click
                click_detected = False  # Reset to make sure isn't already clicked

        # If not waiting for a click, make a new wait time
        if not waiting_for_click and reaction_start_time is None:
            cnt = random.randint(1, 10) * 1000  # Random delay in MILLESECONDS
            reaction_start_time = pygame.time.get_ticks() + cnt  # Set time to make screen white

        # Check if a click happened when screen white
        if waiting_for_click:
            elapsed_time = (pygame.time.get_ticks() - start_time) / 1000  # Convert milleseconds to seconds
            if click_detected:

                #Add to score and rounds
                rounds += 1
                score += 1
                print("Click detected in time! Score increased.")  
                waiting_for_click = False  # Reset reaction phase
                screen.fill("black")
                pygame.display.flip()
            elif elapsed_time > round((random.uniform(0.1,1)), 2):  # If it was not clicked in random amount of time, 0.1-1 seconds long
                rounds += 1
                print("Too slow!")
                waiting_for_click = False  # Reset reaction phase
                screen.fill("black")
                pygame.display.flip()

        clock.tick(60)  # Limit FPS to 60

    pygame.quit()
    print(f"{score}/{rounds}")

    #This is Luke's part
    return repeat

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

def clicky(rct, repeat):
    score = 0
    rounds = 0
    pygame.init()
    screen = pygame.display.set_mode((1280, 720)) #Change this to make the display bigger, or not as big
    clock = pygame.time.Clock() #Sets the base time to that of Pygame's
    running = True
    click_detected = False
    waiting_for_click = False
    start_time = None
    reaction_start_time = None

    while running:
        screen.fill("black")

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #If they click the X, ends the game
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and waiting_for_click:
                mouse_x, mouse_y = pygame.mouse.get_pos()  # Get mouse position
                if rct.rect.collidepoint(mouse_x, mouse_y):  # Check if click is inside the sprite
                    click_detected = True
                    score += 1  # Increase score since click was inside the sprite
                    print("Score increased.")

        if reaction_start_time is not None:
            if pygame.time.get_ticks() >= reaction_start_time:
                rct.randomize_position() #Randomises position of rectangle
                screen.blit(rct.image, (rct.rect.x, rct.rect.y)) #Shows rectangle
                pygame.display.flip()
                start_time = pygame.time.get_ticks() #Gets the start time
                reaction_start_time = None
                waiting_for_click = True
                click_detected = False

        if not waiting_for_click and reaction_start_time is None:
            cnt = random.randint(1, 10) * 1000 #Find time to delay for between 1 and 10 seconds
            reaction_start_time = pygame.time.get_ticks() + cnt #Delay for that much time from current time

        if waiting_for_click: #If box has appeared
            elapsed_time = (pygame.time.get_ticks() - start_time) / 1000 #The time since the start time
            if click_detected: #If there is a click
                rounds += 1
                print(f"Round {rounds} complete! Score: {score}")
                waiting_for_click = False
                screen.fill("black")
                pygame.display.flip()
            elif elapsed_time > round(random.uniform(0.3, 1.5), 2): #Tweak these numbers to change timing of box
                rounds += 1
                print("Too slow! Not clicked!")
                waiting_for_click = False
                screen.fill("black")
                pygame.display.flip()

        clock.tick(60) #How fast game ticks

    pygame.quit()
    #This is Luke's part
    return rct, repeat




def guess_1_4(repeat):
    rpt = input("How many rounds would you like to play?\n")
    try:
        rpt = int(rpt)
    except:
        return ("That is not a valid answer! Make sure it is an integer!")
    score = 0
    rounds = 0
    while rpt > 0:
        gs = int(input("\n\nGuess a number 1-4!\n")) #Get user guess
        cgs = random.randint(1,4) #Computer guesses a number
        if gs == cgs: #If numbers are the same
            score += 1
            rounds += 1
            print("You guessed the computer's number!")
            print(score,"/",rounds)
            rpt -= 1
        else: #If numbers are not the same
            rounds += 1
            print("You did not guess the correct number!")
            print(score,"/",rounds)
            rpt -= 1
    print("\n\n\n",score,"/",rounds)
    print("This is your final score")
    #This is Luke's part
    return repeat

def main(repeat):
    ans = input("Which game would you like to play?\n    1 for reaction test box\n    2 for number guess\n    3 for reaction test regular\n    4 for exit\n    Answer here: ")
    if ans == "1":
        rct = Clicked("white", 200, 200)  
        rct, repeat = clicky(rct, repeat)
    elif ans == "2":
        repeat = guess_1_4(repeat)
    elif ans == "3":
        repeat = react_test(repeat)
    else:
        print("Goodbye!")
        repeat = 0
    return repeat
while repeat > 0:
    main(repeat)