# Define a function to control movement of ball
def ball_movement(x, y, height, ball):
    '''
    x (int): Integer defining the movement direction on x axis
    y (int): Integer defining the movement direction on y axis
    height (int): Defines the height of the playing window
    width (int): Defines the width of the playing window
    ball (Ball): The ball object of class Ball

    Returns:
    y_invert (int): Inverted movement in y-axis direction when ball hits frame
    '''

    # New Ball position
    ball.set_position(x, y)

    # If ball touches upper frame
    if ball.get_position()[1] + ball.get_size() == height:
        # invert y movement
        y_invert = y * -1
        return y_invert

    # If ball touches lower frame
    elif ball.get_position()[1] - ball.get_size() == 0:
        # invert y movement
        y_invert = y * -1
        return y_invert

    # If nothing of the above happens
    else:
        return y

