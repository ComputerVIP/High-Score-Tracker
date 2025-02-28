import pygame
import random
from add_scores import add_score
import csv

def clicky(rct):
    print("You will need to click the white box as it appears to make your score increase!")
    game_name = "Box" # Hard reaction test

    score = 0
    rounds = 0
    pygame.init()
    screen = pygame.display.set_mode((1280, 720)) #Change this to make the display bigger, or not as big
    pygame.display.set_caption('Pygame Window')

    # Make sure the display is updated
    pygame.display.flip()

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
                print(f"Click detected!\n{score}/{rounds}\n")
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
    print(f'\n\nFinal score:\n{score}/{rounds}')

    with open("Scores.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header line
        users = []
        
        # Collect user data
        for row in reader:
            # Assuming that row[1] is the name and row[ans + 1] is the score for the selected game
            users.append([row[1], row[3]])  # row[1] -> name, row[ans + 1] -> score
        
        # Sort users based on the score in descending order
        sorted_users = sorted(users, key=lambda user: int(user[1]), reverse=True)
        
        # Print the sorted scores
        for user in sorted_users:
            print(f"{user[1]} {user[0]}")
            count += 1
            if count >10:
                break
    add_score(score, game_name)
    return