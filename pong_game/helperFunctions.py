# Import required packages
import random

# Import Parameters
import pygame.time

from parameters import *


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
        x_direction, y_direction, ball, score, left_paddle, right_paddle, score_time,
        pong_sound, win_sound, loss_sound):
    '''
    x_direction (int): Integer defining the movement direction on x axis
    y_direction (int): Integer defining the movement direction on y axis
    height (int): Defines the height of the playing window
    width (int): Defines the width of the playing window
    ball (Ball): The ball object of class Ball
    score (list): A list with two elements, the score of left and right players
    left_paddle (PaddleLeft): The left paddle object of class Paddle
    right_paddle (PaddleRight): The right paddle object of class Paddle
    score_time (double or None): Time when last goal was scored
    pong_sound (WAV): Sound when ball hits paddle
    win_sound (WAV): Sound when player wins
    loss_sound(WAV): Sound when player loses

    Returns:
    y_direction (int): Movement direction on y-axis after checking all conditions
    x_direction (int): Movement direction on x-axis after checking all conditions
    score (list): Contains the scores of each player
    score_time (double or None): Time when last goal was scored. 
    '''

    # New Ball position
    ball.set_position(x_direction, y_direction)

    # If ball touches upper edge
    if ball.get_position()[1] + ball.get_size() > HEIGHT:
        # invert y movement
        y_direction = y_direction * -1
        return x_direction, y_direction, score, score_time

    # If ball touches lower edge
    elif ball.get_position()[1] - ball.get_size() < 0:
        # invert y movement
        y_direction = y_direction * -1
        return x_direction, y_direction, score, score_time

    # If player scores
    elif ball.get_position()[0] - ball.get_size() > WIDTH:
        # Increase score of right player
        score[0] += 1
        # Play sound if goal means loss
        if score[0] == POINTS_TO_WIN:
            pygame.mixer.Sound.play(win_sound)
        # get score time
        score_time = pygame.time.get_ticks()
        x_direction = random.sample([1, -1], 1)[0] * 1.5  # Horizontal movement (left or right)
        y_direction = random.sample([random.uniform(-1, -0.5), random.uniform(0.5, 1)], 1)[0] * 1.5  # Vertical movement (down or up)

        return x_direction, y_direction, score, score_time

    # If player gets scored on
    elif ball.get_position()[0] + ball.get_size() < 0:
        # Increase score of right player
        score[1] += 1
        # Play sound if goal means loss
        if score[1] == POINTS_TO_WIN:
            pygame.mixer.Sound.play(loss_sound)
        # get score time
        score_time = pygame.time.get_ticks()
        x_direction = random.sample([1, -1], 1)[0] * 1.5  # Horizontal movement (left or right)
        y_direction = random.sample([random.uniform(-1, -0.5), random.uniform(0.5, 1)], 1)[0] * 1.5  # Vertical movement (down or up)

        return x_direction, y_direction, score, score_time

    # If ball touches a paddle
    elif collision(left_paddle, right_paddle, ball):

        # If ball speed is still below maximal speed
        if abs(x_direction) < 5:

            # invert x movement with multiplier
            x_direction = x_direction * -1.25
            y_direction = y_direction * 1.25


        # If ball speed is above maximal speed
        elif abs(x_direction) > 5:

            # invert x movement without multiplier
            x_direction = x_direction * -1
            y_direction = y_direction * 1

        ball.set_color(random.sample(range(0, 256, 1), 3))
        left_paddle.set_color(random.sample(range(0, 256, 1), 3))
        right_paddle.set_color(random.sample(range(0, 256, 1), 3))
        pygame.mixer.Sound.play(pong_sound)
        return x_direction, y_direction, score, score_time

    # If nothing of the above happens
    else:
        return x_direction, y_direction, score, score_time


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


# Create an AI to decide on how to move the paddle
def ai_movement(right_paddle, ball, x_direction, y_direction):
    '''
    right_paddle (PaddleRight): Right paddle Object
    ball (Ball): Ball object
    x_direction (int): Integer defining the movement direction of the ball on x axis
    y_direction (int): Integer defining the movement direction of the ball on y axis

    Returns:
    ai_command (int): Command of AI to move paddle up or down
    '''

    # If ball is moving to the right
    if x_direction > 0:

        # Get current ball position
        position = ball.get_position()

        # Calculate final contact point of ball with right edge
        contact_point = position[1] + (y_direction / x_direction) * (WIDTH - position[0])

        # Add random movement to AI to prevent it from being to strong
        contact_point += random.normalvariate(0, OPPONENT_ADVANCED)

        # If y position of paddle to high
        if right_paddle.position[1] > contact_point:
            ai_command = -3

        # If y position of paddle to low
        elif right_paddle.position[1] < contact_point:
            ai_command = 3

        # If position correct
        else:
            ai_command = 0

    # If ball is moving to the left
    if x_direction < 0:
        ai_command = 0

    return ai_command
