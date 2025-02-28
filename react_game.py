import pygame
import random
from add_scores import add_score

def react_test():
    print("Click the screen when it is white to make the score increase!")
    game_name = "React"  # Easy reaction test

    # Variables to keep track of the score and amount of rounds
    score = 0
    rounds = 0
    counter = 0

    # Initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption('Pygame Window')
    clock = pygame.time.Clock()
    running = True


    pygame.display.set_caption('Pygame Window')

# Make sure the display is updated
    pygame.display.flip()

    click_detected = False
    waiting_for_click = False
    start_time = None  
    reaction_start_time = None  # Timer for reaction delay
    check = None  # Variable to hold the score before waiting period

    while running:
        screen.fill("black")  # Clear the screen to black

        # Handle Pygame events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if waiting_for_click:
                    click_detected = True
                else:
                    counter += 1
                    print(f"Clicked early, you are at {counter}/5 misclicks")
                    if counter >= 5:
                        score -= 1  # Penalize early clicks
                        print("Score reduced! Don't click too soon.")
                        counter = 0

        # If waiting for the delay before reaction starts
        if reaction_start_time is not None:
            if pygame.time.get_ticks() >= reaction_start_time:  # Check if delay is over
                screen.fill("white")  # Screen goes white
                pygame.display.flip()
                start_time = pygame.time.get_ticks()  # Start reaction timer
                reaction_start_time = None  # Stop timer to wait random amount of time

                waiting_for_click = True  # Wait for click
                click_detected = False  # Reset to make sure isn't already clicked

        # If not waiting for a click, make a new wait time
        if not waiting_for_click and reaction_start_time is None:
            cnt = random.randint(1, 10) * 1000  # Random delay in MILLESECONDS
            reaction_start_time = pygame.time.get_ticks() + cnt  # Set time to make screen white

        # Check if a click happened when screen white
        if waiting_for_click:
            elapsed_time = (pygame.time.get_ticks() - start_time) / 1000  # Convert milliseconds to seconds

            if click_detected:
                if check is None:  # First valid click
                    check = score  # Set 'check' to the current score on first click
                    score += 1  # Add score on first valid click
                    print("First click detected, score increased!")
                else:
                    print("Click detected, but no score change during waiting.")
                
                # Reset reaction phase
                waiting_for_click = False
                screen.fill("black")  # Fill the screen black after click
                pygame.display.flip()  # Show the black screen
            elif elapsed_time > round(random.uniform(0.1, 1), 2):  # If it was not clicked in random amount of time, 0.1-1 seconds long
                rounds += 1
                print("Too slow!")
                screen.fill("black")  # Fill the screen black if too slow
                pygame.display.flip()  # Show the black screen
                waiting_for_click = False  # Reset reaction phase

        clock.tick(60)  # Limit FPS to 60

    pygame.quit()
    print(f"{score}/{rounds}")
    if score < 0:
        score = 0
    add_score(score, game_name)
    return
