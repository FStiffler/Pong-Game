# Import Parameters
from parameters import *

# Define Ball class
class Ball(object):
    def __init__(self, color, size=10):
        '''
        Initializes a Ball object

        color (tuple): A tuple with RGB values
        size (int): Integer defining the size of ball, default = 10

        A Ball object has the following attribute:
            self.color (tuple, determined by input tuple)
            self.size (int, determined by size)
            self.position (tuple, defines start position of ball)

        '''
        self.color = color
        self.size = size
        self.position = (WIDTH // 2, HEIGHT // 2)

    def set_color(self, color):
        '''
        Changes color of Ball object

        color (tuple): A tuple with RGB values

        Changes attribute: self.color
        '''
        self.color = color

    def get_color(self):
        '''
        Get color of Ball object

        Returns: self.color
        '''
        return self.color

    def set_size(self, size):
        '''
        Changes size of Ball object

        size (int): Integer defining the size of ball

        Changes attribute: self.size
        '''
        self.size = size

    def get_size(self):
        '''
        Get size of Ball object

        Returns: self.size
        '''
        return self.size

    def set_position(self, x, y):
        '''
        Changes position of Ball object (animation of ball)

        x (int): Integer defining the movement direction on x axis
        y (int): Integer defining the movement direction on y axis

        Changes attribute: self.position
        '''
        new_x = self.position[0]+x
        new_y = self.position[1]+y
        self.position = (new_x, new_y)

    def get_position(self):
        '''
        Get start position of Ball object

        Returns: self.position
        '''
        return self.position


# Define parent class for paddles
class Paddle(object):
    def __init__(self, color):
        '''
        Initializes a Paddle object

        color (tuple): A tuple with RGB values

        A Paddle object has the following attribute:
            self.color (tuple, determined by input tuple)

        '''
        self.color = color

    def set_color(self, color):
        '''
        Changes color of Paddle object

        color (tuple): A tuple with RGB values

        Changes attribute: self.color
        '''
        self.color = color

    def get_color(self):
        '''
        Get color of Paddle object

        Returns: self.color
        '''
        return self.color


# Define left paddle child class
class PaddleLeft(Paddle):

    # define parameters of paddle
    def __init__(self, color):
        '''
        Initializes a PaddleLeft object

        color (tuple): A tuple with RGB values

        A PaddleLeft object has the following attributes:
            self.color (tuple, determined by input tuple)
            self.position (list, starting coordinates of paddle)
            self.top_left (tuple, coordinates of top left corner of paddle)
            self.top_right (tuple, coordinates of top right corner of paddle)
            self.down_right (tuple, coordinates of down right corner of paddle)
            self.down_left (tuple, coordinates of down right corner of paddle)
        '''
        Paddle.__init__(self, color)
        self.position = [PAD_WIDTH_HALF + 0.01 * WIDTH, HEIGHT // 2]
        self.top_left = (self.position[0] - PAD_WIDTH_HALF, self.position[1] + PAD_HEIGHT_HALF)
        self.top_right = (self.position[0] + PAD_WIDTH_HALF, self.position[1] + PAD_HEIGHT_HALF)
        self.down_right = (self.position[0] + PAD_WIDTH_HALF, self.position[1] - PAD_HEIGHT_HALF)
        self.down_left = (self.position[0] - PAD_WIDTH_HALF, self.position[1] - PAD_HEIGHT_HALF)

    def get_polygon(self):
        '''
        Get list of corner points of polygon shape

        Returns: [self.top_left,self.top_right,self.down_right,self.down_left]
        '''
        return [self.top_left, self.top_right, self.down_right, self.down_left]


# Define right paddle child class
class PaddleRight(Paddle):

    # define parameters of paddle
    def __init__(self, color):
        '''
        Initializes a PaddleRight object

        color (tuple): A tuple with RGB values

        A PaddleRight object has the following attributes:
            self.color (tuple, determined by input tuple)
            self.position (list, starting coordinates of paddle)
            self.top_left (tuple, coordinates of top left corner of paddle)
            self.top_right (tuple, coordinates of top right corner of paddle)
            self.down_right (tuple, coordinates of down right corner of paddle)
            self.down_left (tuple, coordinates of down right corner of paddle)
        '''
        Paddle.__init__(self, color)
        self.position = [WIDTH - PAD_WIDTH_HALF - 0.01 * WIDTH, HEIGHT // 2]
        self.top_left = (self.position[0] - PAD_WIDTH_HALF, self.position[1] + PAD_HEIGHT_HALF)
        self.top_right = (self.position[0] + PAD_WIDTH_HALF, self.position[1] + PAD_HEIGHT_HALF)
        self.down_right = (self.position[0] + PAD_WIDTH_HALF, self.position[1] - PAD_HEIGHT_HALF)
        self.down_left = (self.position[0] - PAD_WIDTH_HALF, self.position[1] - PAD_HEIGHT_HALF)

    def get_polygon(self):
        '''
        Get list of corner points of polygon shape

        Returns: [self.top_left,self.top_right,self.down_right,self.down_left]
        '''
        return [self.top_left, self.top_right, self.down_right, self.down_left]


if __name__ == '__main__':

    ball = Ball(WHITE)
    left = PaddleLeft(WHITE)
    right = PaddleRight(WHITE)