# Import packages
import pygame
import random

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

# Initialize sounds
pong_sound = pygame.mixer.Sound('laser.wav')
goal_sound = pygame.mixer.Sound('goal.wav')
received_sound = pygame.mixer.Sound('received_goal.wav')

# Initialize game window
screen = pygame.display.set_mode(size=(WIDTH, HEIGHT))

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
    screen.fill(BLACK)

    # Drawing ######

    # Draw a center line
    pygame.draw.line(screen, WHITE, start_pos=(WIDTH // 2, HEIGHT), end_pos=(WIDTH // 2, 0))

    # Draw circle in in middle
    pygame.draw.circle(screen, WHITE, center=(WIDTH // 2, HEIGHT // 2), radius=WIDTH * 0.1, width=1)

    # Draw the ball
    pygame.draw.circle(screen, color=ball.get_color(), center=ball.get_position(), radius=ball.get_size())

    # Draw paddle on the left
    pygame.draw.polygon(screen, color=left_paddle.get_color(), points=left_paddle.get_polygon())

    # Draw paddle on the right
    pygame.draw.polygon(screen, color=right_paddle.get_color(), points=right_paddle.get_polygon())

    # Animation #####

    # As long as game not over
    if playing:

        # Move ball
        x_direction, y_direction, score, score_time = \
            ball_movement(x_direction, y_direction, ball, score, left_paddle, right_paddle,
                          score_time, pong_sound, goal_sound, received_sound)

        # In case of goal start timer before ball is released once again
        if score_time:
            score_time = ball.set_back(score_time)

        # Move paddle based on captured movement command of user
        command = paddle_movement(command, HEIGHT, left_paddle)

        # Return AI command for right paddle movement
        ai_command = ai_movement(right_paddle, ball, x_direction, y_direction)

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
        message_font_main = pygame.font.SysFont("Comic Sans MS", 100)
        message_font_minor = pygame.font.SysFont("Comic Sans MS", 20)
        main_message = message_font_main.render("You Lost!", 1, WHITE)
        minor_message = message_font_minor.render("Click 'Enter' to play again", 1, WHITE)
        main_message_rect = main_message.get_rect()
        minor_message_rect = minor_message.get_rect()
        main_message_rect.center = (WIDTH/2, HEIGHT/2)
        minor_message_rect.center = (WIDTH/2, HEIGHT/2+200)
        screen.blit(main_message, main_message_rect)
        screen.blit(minor_message, minor_message_rect)

        # Event key
        for event in pygame.event.get():

            # Capture commands by user to move paddle (User holds arrow key to move paddle)
            if event.type == pygame.KEYDOWN:

                # Let user end game by clicking on close button
                if event.type == pygame.QUIT:
                    running = False

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
