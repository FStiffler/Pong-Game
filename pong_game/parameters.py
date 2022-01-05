import random

# Define Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


# Define constants
WIDTH = 1440
HEIGHT = 900
PAD_WIDTH = 20
PAD_HEIGHT = 200
PAD_WIDTH_HALF = PAD_WIDTH // 2
PAD_HEIGHT_HALF = PAD_HEIGHT // 2
OPPONENT_HARD = 100
OPPONENT_ADVANCED = 250
OPPONENT_EASY = 500
POINTS_TO_WIN = 2

# Define global variables
x_direction = random.sample([1, -1], 1)[0]*1.5  # Initial horizontal movement (left or right)
y_direction = \
    random.sample([random.uniform(-1, -0.5), random.uniform(0.5, 1)], 1)[0]*1.5  # Initial vertical movement (down or up)
command = 0  # paddle movement variable
score = [0, 0]  # score variable
score_time = None  # score time variable
running = True  # Running variable
playing = True