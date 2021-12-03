# Import packages
import pygame

# Initialize pygame
pygame.init()

# Define Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Define constants
WIDTH = 1000
HEIGHT = 500
PAD_WIDTH = 20
PAD_HEIGHT = 200
PAD_WIDTH_HALF = PAD_WIDTH // 2
PAD_HEIGHT_HALF = PAD_HEIGHT // 2

# Global variables
padl_position = [PAD_WIDTH_HALF + 0.01 * WIDTH, HEIGHT // 2]  # Initial position of left paddle
padr_position = [WIDTH - PAD_WIDTH_HALF - 0.01 * WIDTH, HEIGHT // 2]  # Initial position of right paddle

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
    pygame.draw.polygon(screen,
                        BLUE,
                        points=[
                            (padl_position[0] - PAD_WIDTH_HALF, padl_position[1] + PAD_HEIGHT_HALF),  # x1&y1 top left
                            (padl_position[0] + PAD_WIDTH_HALF, padl_position[1] + PAD_HEIGHT_HALF),  # x2&y2 top right
                            (padl_position[0] + PAD_WIDTH_HALF, padl_position[1] - PAD_HEIGHT_HALF),  # x3&y3 down right
                            (padl_position[0] - PAD_WIDTH_HALF, padl_position[1] - PAD_HEIGHT_HALF),  # x4&y4 down left
                                ]
                        )

    # Draw paddle on the right
    pygame.draw.polygon(screen,
                        BLUE,
                        points=[
                            (padr_position[0] - PAD_WIDTH_HALF, padr_position[1] + PAD_HEIGHT_HALF),  # x1&y1 top left
                            (padr_position[0] + PAD_WIDTH_HALF, padr_position[1] + PAD_HEIGHT_HALF),  # x2&y2 top right
                            (padr_position[0] + PAD_WIDTH_HALF, padr_position[1] - PAD_HEIGHT_HALF),  # x3&y3 down right
                            (padr_position[0] - PAD_WIDTH_HALF, padr_position[1] - PAD_HEIGHT_HALF),  # x4&y4 down left
                        ]
                        )

    # Flip the display
    pygame.display.flip()
