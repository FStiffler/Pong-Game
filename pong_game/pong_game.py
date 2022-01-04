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

    # game events
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

    # Draw a center line
    pygame.draw.line(screen, WHITE, start_pos=(WIDTH // 2, HEIGHT), end_pos=(WIDTH // 2, 0))

    # Draw circle in in middle
    pygame.draw.circle(screen, WHITE, center=(WIDTH // 2, HEIGHT // 2), radius=WIDTH * 0.1, width=1)

    # Draw the ball at center of field
    pygame.draw.circle(screen, color=ball.get_color(), center=ball.get_position(), radius=ball.get_size())

    # Move ball
    x_direction, y_direction, score, score_time = \
        ball_movement(x_direction, y_direction, WIDTH, HEIGHT, ball, score, left_paddle, right_paddle,
                      score_time, pong_sound, goal_sound, received_sound)

    # In case of goal start timer before ball is released once again
    if score_time:
        score_time = ball.set_back(score_time)

    # Draw paddle on the left
    pygame.draw.polygon(screen, color=left_paddle.get_color(), points=left_paddle.get_polygon())

    # Move paddle based on captured movement command of user
    command = paddle_movement(command, HEIGHT, left_paddle)

    # Draw paddle on the right
    pygame.draw.polygon(screen, color=right_paddle.get_color(), points=right_paddle.get_polygon())

    # Return AI command for right paddle movement
    ai_command = ai_movement(right_paddle, ball, x_direction, y_direction)

    # Move paddle based on proposed movement command of AI
    ai_command = paddle_movement(ai_command, HEIGHT, right_paddle)

    # Define refresh time
    clock.tick(300)

    # Score Boards in Window
    myfont1 = pygame.font.SysFont("Comic Sans MS", 20)
    label1 = myfont1.render("Score: " + str(score[0]), 1, WHITE)
    screen.blit(label1, (0.25*WIDTH-30, 10))

    myfont2 = pygame.font.SysFont("Comic Sans MS", 20)
    label2 = myfont2.render("Score: " + str(score[1]), 1, WHITE)
    screen.blit(label2, (0.75*WIDTH-30, 10))

    # Flip the display
    pygame.display.flip()
