# Import packages
import pygame
import random

# Import modules
from parameters import *
from classes import *
from helperFunctions import *

# Initialize pygame
pygame.init()

# Create objects from pre-defined classes
left_paddle = PaddleLeft(BLUE)
right_paddle = PaddleRight(BLUE)
ball = Ball(RED)

# Create random movement direction of ball
x_direction = random.sample([1, -1], 1)[0]  # Randomly define movement to left or right
y_direction = random.uniform(-1, 1)  # Ball moves with maximal slope of 1

# Initalize game window
screen = pygame.display.set_mode(size=(WIDTH, HEIGHT))

# Set title
pygame.display.set_caption("Pong Game")

# Define a running variable
running = True

# Define window refresh parameter
clock = pygame.time.Clock()

# Run game until user wants to drop out
while running:

    # game events
    for event in pygame.event.get():

        # Let user end game by clicking on close button
        if event.type == pygame.QUIT:
            running = False

    # Define color of background
    screen.fill(BLACK)

    # Draw a center line
    pygame.draw.line(screen, WHITE, start_pos=(WIDTH // 2, HEIGHT), end_pos=(WIDTH // 2, 0))

    # Draw circle in in middle
    pygame.draw.circle(screen, WHITE, center=(WIDTH // 2, HEIGHT // 2), radius=WIDTH * 0.1, width=1)

    # Draw the ball at center of field
    pygame.draw.circle(screen, color=ball.get_color(), center=ball.get_position(), radius=ball.get_size())

    # Move ball
    x_direction, y_direction = ball_movement(x_direction, y_direction, WIDTH, HEIGHT, ball)

    # Draw paddle on the left
    pygame.draw.polygon(screen, color=left_paddle.get_color(), points=left_paddle.get_polygon())

    # Draw paddle on the right
    pygame.draw.polygon(screen, color=right_paddle.get_color(), points=right_paddle.get_polygon())

    # Define refresh time
    clock.tick(500)

    # Flip the display
    pygame.display.flip()
