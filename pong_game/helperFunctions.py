# Import required packages
import random


# Define collision function
def collision(left_paddle, right_paddle, ball):
    '''
    ball (Ball): The ball object of class Ball
    left_paddle (PaddleLeft): The left paddle object of class Paddle
    right_paddle (PaddleRigth): The right paddle object of class Paddle

    Returns:
    Boolean value for collision
    '''

    # Define object position
    ball_position = ball.get_position()
    ball_radius = ball.get_size()
    pl_top_position = left_paddle.top_right[1]
    pl_down_position = left_paddle.down_right[1]
    pl_right_position = left_paddle.down_right[0]
    pr_top_position = right_paddle.top_left[1]
    pr_down_position = right_paddle.down_left[1]
    pr_left_position = right_paddle.down_left[0]

    # Return True if collision has occured
    if ball_position[0] - ball_radius <= pl_right_position and \
            pl_down_position <= ball_position[1] <= pl_top_position:
        return True

    # Return True if collision has occured
    if ball_position[0] + ball_radius >= pr_left_position and \
            pr_down_position <= ball_position[1] <= pr_top_position:
        return True

    # Return False otherwise
    else:
        return False


# Define a function to control movement of ball
def ball_movement(
        x_direction, y_direction, width, height, ball, score, left_paddle, right_paddle):
    '''
    x_direction (int): Integer defining the movement direction on x axis
    y_direction (int): Integer defining the movement direction on y axis
    height (int): Defines the height of the playing window
    width (int): Defines the width of the playing window
    ball (Ball): The ball object of class Ball
    score (list): A list with two elements, the score of left and right players
    left_paddle (PaddleLeft): The left paddle object of class Paddle
    right_paddle (PaddleRight): The right paddle object of class Paddle

    Returns:
    y_direction (int): Movement direction on y-axis after checking all conditions
    x_direction (int): Movement direction on x-axis after checking all conditions
    '''

    # New Ball position
    ball.set_position(x_direction, y_direction)

    # If ball touches upper edge
    if ball.get_position()[1] + ball.get_size() > height:
        # invert y movement
        y_direction = y_direction * -1
        return x_direction, y_direction, score

    # If ball touches lower edge
    elif ball.get_position()[1] - ball.get_size() < 0:
        # invert y movement
        y_direction = y_direction * -1
        return x_direction, y_direction, score

    # If ball touches right edge
    elif ball.get_position()[0] - ball.get_size() > width:
        # Initialize ball a midpoint again
        ball.set_back()
        #  New ball direction
        x_direction = random.sample([1, -1], 1)[0]  # Horizontal movement (left or right)
        y_direction = random.uniform(-1, 1)  # Vertical movement (down or up)
        # Increase score of left player
        score[0] += 1

        return x_direction, y_direction, score

    # If ball touches left edge
    elif ball.get_position()[0] + ball.get_size() < 0:
        # Initialize ball a midpoint again
        ball.set_back()
        #  New ball direction
        x_direction = random.sample([1, -1], 1)[0]  # Horizontal movement (left or right)
        y_direction = random.uniform(-1, 1)  # Vertical movement (down or up)
        # Increase score of right player
        score[1] += 1

        return x_direction, y_direction, score

    # If ball touches a paddle
    elif collision(left_paddle, right_paddle, ball):
        # invert x movement
        x_direction = x_direction * -1.25
        return x_direction, y_direction, score

    # If nothing of the above happens
    else:
        return x_direction, y_direction, score


# Define a function to control movement of paddle
def paddle_movement(command, height, paddle):
    '''
    command (int): Integer defining the movement direction on x axis
    height (int): Defines the height of the playing window
    paddle (Paddle): The paddle object of class Paddle

    Returns:
    command (int): Integer defining the movement after command was executed
    '''

    # New Paddle Position
    paddle.set_position(command)

    # get height of top left corner
    top_left_height = paddle.get_polygon()[0][1]

    # get height of down left corner
    down_left_height = paddle.get_polygon()[3][1]

    # Stop upward movement when upper edge is touched
    if top_left_height == height:
        command = 0

    # Stop upward movement when upper edge is touched
    if down_left_height == 0:
        command = 0

    return command
