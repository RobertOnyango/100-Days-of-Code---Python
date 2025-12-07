# A class Scoreboard from Turtle that keeps track of how many food items are eaten by the snake i.e. keeps track of the score and shows how it is displayed

from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        
        # The score is zero intially
        self.score = 0
        # Variable to hold the high score
        self.high_score = self.get_high_score()
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
        self.clear()
        self.write(f"Score = {self.score} High Score = {self.high_score}", align=ALIGNMENT, font=FONT)

    # Function that increases the score
    def increase_scores(self):
        self.score += 1
        # Call the update_scores function to create a new scoreboard with the new score
        self.create_scoreboard()

    # Function that reads the file data.txt and returns the value as the high_score
    def get_high_score(self):
        # Open the file
        with open("data.txt") as data:
            # Read the contents of the file 
            contents = data.read()
        # Return the contents of the file as an integer
        return int(contents)

    # Function that updates the high score
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            # Update the data file to have new high score
            with open("data.txt", mode="w") as data:
                data.write(str(self.high_score))
        # Reset score to zero after updating high score
        self.score = 0
        # Create the new updated scoreboard
        self.create_scoreboard()