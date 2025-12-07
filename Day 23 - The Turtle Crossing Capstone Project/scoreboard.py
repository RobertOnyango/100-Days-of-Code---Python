# A ScoreBoard class that writes the level the user currently is on (an increase in game level -> an increase in the speed of the cars moving across the screen) and writes Game Over when the player touches one of the random cars

from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        # Initialize the first score
        self.level = 1
        # Set the scoreboard to the leftmost corner
        self.goto(-280, 250)
        self.create_scoreboard()

    # Function that create the scoreboard
    def create_scoreboard(self):
        self.write(f"Level: {self.level}", align="left", font=FONT)
    
    # Functiion that will write on scree the increased level
    def increase_level(self):
        self.level += 1
        # Clear initial scoreboard
        self.clear()
        # Create the new scoreboard with the new level
        self.create_scoreboard()

    # Function that outputs the game over text upon collition of player with car
    def game_over(self):
        # Place it a the center of the screen
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)
