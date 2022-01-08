import random
import os

# Define Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Define constants
WIDTH = 1024
HEIGHT = 576
PAD_WIDTH = 20
PAD_HEIGHT = 200
PAD_WIDTH_HALF = PAD_WIDTH // 2
PAD_HEIGHT_HALF = PAD_HEIGHT // 2
OPPONENT_HARD = 100
OPPONENT_ADVANCED = 700
OPPONENT_EASY = 1500
POINTS_TO_WIN = 5
COOLDOWN = 1500
PADDLESPEED = 3
ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))

# Define global variables
x_direction = random.sample([1, -1], 1)[0]*1.5  # Initial horizontal movement (left or right)
y_direction = \
    random.sample([random.uniform(-1, -0.5), random.uniform(0.5, 1)], 1)[0]*1.5  # Initial vertical movement (down or up)
command = 0  # paddle movement variable
score = [0, 0]  # score variable
score_time = None  # score time variable
running = True  # Running variable
playing = False  # Play variable to differentiate between in game and out of game action
choose_difficulty = False  # Variable to enter screen to choose difficulty
start = True  # Startscreen only showing once when starting the game
drawing = False  # Variable to turn-off drawing as long as there is game going on