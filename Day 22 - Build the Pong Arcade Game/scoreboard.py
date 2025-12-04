# A Class that holds teh Scoreboard for the Ping Pong game. Inherits from the Turtle class. Each player's side will have a score object

from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    # Function that creates the scoreboard
    def update_scoreboard(self):
        self.clear()
        # Left sides score
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        # Right sides score
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)
    
    # Function that increases left side's score when the right paddle misses
    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()
    
    # Function that increases right side's score when the lefty paddle misses
    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()