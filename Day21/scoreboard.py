from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.score_A = 0
        self.score_B = 0

    def update_scoreboard(self):
        self.clear()
        self.goto(-300, 250)
        self.write(f"Score A:{self.score_A}", font=("Courier", 20, "normal"))
        self.goto(150, 250)
        self.write(f"Score B:{self.score_B}", font=("Courier", 20, "normal"))

    def point_a(self):
        self.score_A += 1
        self.update_scoreboard()

    def point_b(self):
        self.score_B += 1
        self.update_scoreboard()
