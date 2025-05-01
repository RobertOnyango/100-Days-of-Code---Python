# Scoreboard class that inherits from the turtle class such that it knows how to keep the score and display it in the program
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
    
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 268)
        self.update_scoreboard()
        self.hideturtle()

    # Function that updates the scoreboard
    def update_scoreboard(self):
        self.write(f"Score: {self.score} ", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    # Function that increases score and writes new score
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()