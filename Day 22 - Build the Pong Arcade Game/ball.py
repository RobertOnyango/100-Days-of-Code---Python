# TODO 4: A Class Ball that will be a ball object in the Ping Pong Game.
# Xtics: width=20, height=20, x_pos=0, y_pos=0. Upon every screen refresh, the ball moves to the right and upwards diagonally

from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
    
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        # Variable that will help increase ball speed whenever it touches a paddle. See the time.sleep(0.1)
        self.move_speed = 0.1
    
    # Make ball move towards the upwards-right diagonal direction
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
            
    # TODO 5: Function that controls the bounce of the ball upon collision with the top and bottom of the screen using the y_axis
    def bounce_y(self):
        # When the ball touches a side, based on the x,y cordinates, the ball should go on the opposite direction. Note the ball is still always in motion
        self.y_move *= -1
    
    # TODO 6: Function that controls the bounce of the ball upon collison with a paddle using the x_axis
    def bounce_x(self):
        self.x_move *= -1
        # Successful collision should increase the speed of the ball
        self.move_speed *= 0.9

    # Function that resets the ball's condition
    def reset(self):
        # Reset the ball's position to the center
        self.goto(0,0)
        # If any player losses and game resets, the ball speed should be reset
        self.move_speed = 0.1
        # Inverse the ball's x-position. Remember the ball is always moving
        self.bounce_x()

        
