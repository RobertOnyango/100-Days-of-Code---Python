# A Python Program that simulates the famous Ping Pong Arcade Game using the python module turtle.
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

# TODO 1: Create the screen
# Create the screen object
screen = Screen()
# Set its background color to black
screen.bgcolor("black")
# Set the screen dimensions
screen.setup(width=800, height=600)
# Set screen title
screen.title("Ping Pong")
# Turn off the screen animation
screen.tracer(0)

# TODO 2: Create and move a paddle and TODO 3: Create another paddle
# Create the two players objects
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# Set the screen to listen for key screen stokes
screen.listen()

# Listen for the Up arrow key and move upwards for player on the right
screen.onkey(r_paddle.go_up, "Up")
# Listen for the Down arrow key and move downwards for player on the right
screen.onkey(r_paddle.go_down, "Down")

# Listen for the w key and move upwards for player on the left
screen.onkey(l_paddle.go_up, "w")
# Listen for the s key and move downwards for player on the left
screen.onkey(l_paddle.go_down, "s")

# Variable for while loop that holds game state
game_is_on = True

# TODO 4: Create the ball 
ball = Ball()

# TODO 8: Create scoreboard object
scoreboard = ScoreBoard()

# while loop helps in updating the screen
while game_is_on:
    time.sleep(ball.move_speed)
    # Update the screen after the paddle has already been created
    screen.update()
    # Make the ball move
    ball.move()

    # TODO 5: Detect collision with the wall and bounce
    # Ball hits top or bottom pane, its y_cor should be negated so it moves it the inverse y_axis direction.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # TODO 6: Detect collision with paddle
    # Using the distance() in Turtle. However, distance() only takes into account the center of the paddle in this case. Therefore, we also need to take into account the length from the center of paddle, up and down and say that if the ball is within this area then it has made contact with the paddle

    # if ball the distance between the ball and the paddle (remember it's the center of the paddle and the paddle's size is 100, so its 49 upwards and 49 downwards essentially) is 50 and the ball is far enough to the left (-340) or right (340), we can say that the ball has hit the paddle hence it should negate the x-axis direction it was moving towards.
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        # Ball bouunce along the x_axis
        ball.bounce_x()

    # TODO 7: Detect when paddle misses and TODO 8: Keep score
    # Checking if the ball has gone out of bounds at the edge of the screen. 
    # Check if right paddle's position is passed (right side misses)
    if ball.xcor() > 380:
        # Call function that resets the ball to position (0,0) and inverses it's x_axis movement so it goes towards the opposite players (l_paddle) side
        ball.reset()
        scoreboard.l_point()
    
    # Check if left paddle's position is passed (left side misses)
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_point()
    

# TODO 1: Set screen to exit on click
screen.exitonclick()