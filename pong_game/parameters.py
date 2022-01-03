import numpy as np

# Define Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0,255,0)
YELLOW = (255,255,0)
RANDOM = list(np.random.choice(range(256), size=3))

# Define constants
WIDTH = 1000
HEIGHT = 500
PAD_WIDTH = 20
PAD_HEIGHT = 200
PAD_WIDTH_HALF = PAD_WIDTH // 2
PAD_HEIGHT_HALF = PAD_HEIGHT // 2