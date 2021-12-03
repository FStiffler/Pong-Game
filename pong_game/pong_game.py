# Import packages
import pygame

# Import modules
from parameters import *
from classes import *

# Initialize pygame
pygame.init()

# Create paddle objects
left_paddle = PaddleLeft(BLUE)
right_paddle = PaddleRight(BLUE)

# Initalize game window
screen = pygame.display.set_mode(size=(WIDTH, HEIGHT))

# Set title
pygame.display.set_caption("Pong Game")

# Define a running variable
running = True

# Run game until user wants to drop out
while running:

    # Let user end game by clicking on close button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Define color of background
    screen.fill(BLACK)

    # Draw a center line
    pygame.draw.line(screen, WHITE, start_pos=(WIDTH // 2, HEIGHT), end_pos=(WIDTH // 2, 0))

    # Draw circle in in middle
    pygame.draw.circle(screen, WHITE, center=(WIDTH // 2, HEIGHT // 2), radius=WIDTH * 0.1, width=1)

    # Draw the ball at center of field
    pygame.draw.circle(screen, RED, (WIDTH // 2, HEIGHT // 2), 10)

    # Draw paddle on the left
    pygame.draw.polygon(screen, color=left_paddle.get_color(), points=left_paddle.get_polygon())

    # Draw paddle on the right
    pygame.draw.polygon(screen, color=right_paddle.get_color(), points=right_paddle.get_polygon())

    # Flip the display
    pygame.display.flip()
