# Import packages
import pygame
from pygame import mixer
import random
import os

# Import modules
from parameters import *
from classes import *
from helperFunctions import *

# Create objects from pre-defined classes
left_paddle = PaddleLeft(BLUE)
right_paddle = PaddleRight(BLUE)
ball = Ball(RED)

# Initialize pygame
pygame.init()

os.path.join(ROOT_DIR, 'ressources/paddle.wav')

# Initialize sounds
pong_sound = mixer.Sound(os.path.join(ROOT_DIR, 'ressources/paddle.wav'))
win_sound = mixer.Sound(os.path.join(ROOT_DIR, 'ressources/win.wav'))
loss_sound = mixer.Sound(os.path.join(ROOT_DIR, 'ressources/loss.wav'))
goal_sound = mixer.Sound(os.path.join(ROOT_DIR, 'ressources/goal.wav'))
edge_sound = mixer.Sound(os.path.join(ROOT_DIR, 'ressources/edge.wav'))

mixer.init()
mixer.music.load(os.path.join(ROOT_DIR, 'ressources/background.wav'))
mixer.music.play()

# Initialize game window
screen = pygame.display.set_mode(size=(WIDTH, HEIGHT))

# Set background image
background_image = pygame.image.load(os.path.join(ROOT_DIR, 'ressources/background.jpg')).convert()

# Set title
pygame.display.set_caption("Pong Game")

# Define window refresh parameter
clock = pygame.time.Clock()

# Run game until user wants to drop out
while running:


    # Game Events ####
    for event in pygame.event.get():

        # Let user end game by clicking on close button
        if event.type == pygame.QUIT:
            running = False

        # Capture commands by user to move paddle (User holds arrow key to move paddle)
        elif event.type == pygame.KEYDOWN:

            # Capture up command
            if event.key == pygame.K_UP:
                command = -3

            # Capture down command
            if event.key == pygame.K_DOWN:
                command = +3

        # Capturing stop command by user (User released arrow key)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                command = 0

    # Define color of background
    screen.blit(background_image, [0, 0])

    # Drawing ######

    # Draw the ball
    pygame.draw.circle(screen, color=ball.get_color(), center=ball.get_position(), radius=ball.get_size())

    # Draw paddle on the left
    pygame.draw.polygon(screen, color=left_paddle.get_color(), points=left_paddle.get_polygon())

    # Draw paddle on the right
    pygame.draw.polygon(screen, color=right_paddle.get_color(), points=right_paddle.get_polygon())

    # If completly new game
    if playing == False and choose_difficulty == True:

        # Print Message
        write_message(screen, "Choose Difficulty", 50, -150, WHITE)
        write_message(screen, "Easy [E]", 30, 150, WHITE)
        write_message(screen, "Advanced [A]", 30, 190, WHITE)
        write_message(screen, "Hard [H]", 30, 230, WHITE)

        # Event key
        for event in pygame.event.get():

            # Let user end game by clicking on close button
            if event.type == pygame.QUIT:
                running = False

            # Capture commands by user to move paddle (User holds arrow key to move paddle)
            if event.type == pygame.KEYDOWN:

                # If user chooses [E]
                if event.key == pygame.K_e:
                    # Opponent difficulty
                    difficulty = OPPONENT_EASY

                # If user chooses [A]
                elif event.key == pygame.K_a:
                    # Opponent difficulty
                    difficulty = OPPONENT_ADVANCED

                # If user chooses [H]
                elif event.key == pygame.K_h:
                    # Opponent difficulty
                    difficulty = OPPONENT_HARD

                # Restart game
                playing = True

                # Turn of difficulty selection screen
                choose_difficulty = False

    # Animation #####

    # As long as game not over
    if playing:

        # Move ball
        x_direction, y_direction, score, score_time = \
            ball_movement(x_direction, y_direction, ball, score, left_paddle, right_paddle,
                          score_time, pong_sound, win_sound, loss_sound, goal_sound, edge_sound)

        # In case of goal start timer before ball is released once again
        if score_time:
            score_time = ball.set_back(score_time)

        # Move paddle based on captured movement command of user
        command = paddle_movement(command, HEIGHT, left_paddle)

        # Return AI command for right paddle movement
        ai_command = ai_movement(right_paddle, ball, x_direction, y_direction, difficulty)

        # Move paddle based on proposed movement command of AI
        ai_command = paddle_movement(ai_command, HEIGHT, right_paddle)

    # Score Board ####
    score_font= pygame.font.SysFont("Comic Sans MS", 20)
    score1 = score_font.render("Score: " + str(score[0]), 1, WHITE)
    screen.blit(score1, (0.25*WIDTH-30, 10))
    score2 = score_font.render("Score: " + str(score[1]), 1, WHITE)
    screen.blit(score2, (0.75*WIDTH-30, 10))

    # When game is over ####

    # If player looses:
    if score[1] == POINTS_TO_WIN:

        # Stop all animations
        playing = False

        # Print Message
        write_message(screen, "YOU LOST!", 100, -160, WHITE)
        write_message(screen, "Click [ENTER] to play again!", 20, 150, WHITE)



        # Event key
        for event in pygame.event.get():

            # Let user end game by clicking on close button
            if event.type == pygame.QUIT:
                running = False

            # Capture commands by user to move paddle (User holds arrow key to move paddle)
            if event.type == pygame.KEYDOWN:

                # Capture command of enter button
                if event.key == pygame.K_RETURN:

                    # Reset score
                    score = [0, 0]

                    # Restart game
                    playing = True

    # If player wins:
    if score[0] == POINTS_TO_WIN:

        # Stop all animations
        playing = False

        # Print Message
        write_message(screen, "YOU WON!", 100, -160, WHITE)
        write_message(screen, "Click [ENTER] to play again", 20, 150, WHITE)

        # Event key
        for event in pygame.event.get():

            # Let user end game by clicking on close button
            if event.type == pygame.QUIT:
                running = False

            # Capture commands by user to move paddle (User holds arrow key to move paddle)
            if event.type == pygame.KEYDOWN:

                # Capture command of enter button
                if event.key == pygame.K_RETURN:
                    # Reset score
                    score = [0, 0]

                    # Restart game
                    playing = True

    # Define refresh time
    clock.tick(300)

    # Flip the display
    pygame.display.flip()
