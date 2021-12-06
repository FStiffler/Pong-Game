# Define a function to control movement of ball
def ball_movement(x_direction, y_direction, width, height, ball):
    '''
    x_direction (int): Integer defining the movement direction on x axis
    y_direction (int): Integer defining the movement direction on y axis
    height (int): Defines the height of the playing window
    width (int): Defines the width of the playing window
    ball (Ball): The ball object of class Ball

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
        return x_direction, y_direction

    # If ball touches lower edge
    elif ball.get_position()[1] - ball.get_size() < 0:
        # invert y movement
        y_direction = y_direction * -1
        return x_direction, y_direction

    # If ball touches right edge
    elif ball.get_position()[0] - ball.get_size() > width:
        # Initialize ball a midpoint again
        ball.set_back()

        return x_direction, y_direction


    # If nothing of the above happens
    else:
        return x_direction, y_direction

