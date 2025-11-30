# A class Scoreboard from Turtle that keeps track of how many food items are eaten by the snake i.e. keeps track of the score and shows how it is displayed

from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        
        # The score is zero intially
        self.score = 0
        # Score object will have the color white
        self.color("white")
        # Don't draw lines as we move the scoreboard to the top of the window
        self.penup()
        # Move scoreboard to top of window
        self.goto(0, 268)
        # Disappear the turtle
        self.hideturtle()
        # Create the first scoreboard
        self.create_scoreboard()

    # Function that creates and updates the scores    
    def create_scoreboard(self):
        self.write(f"Score = {self.score} ", align=ALIGNMENT, font=FONT)

    # Function that increases the score
    def increase_scores(self):
        self.score += 1
        # Clear the current scoreboard object
        self.clear()
        # Call the update_scores function to create a new scoreboard with the new score
        self.create_scoreboard()
    
    # Funtion that displays to the user that the game is over
    def game_over(self):
        # The game over output should be at the center of the Window
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
    