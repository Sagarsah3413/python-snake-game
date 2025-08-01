from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier",16,"normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0,270)
        self.score = 0
        self.color("white")
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score: {self.score} ", True, align=ALIGNMENT,font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f" - GAME OVER - ", True, align=ALIGNMENT,font=FONT)


    def increase_score(self):
        self.score += 1
        self.goto(0,270)
        self.clear()
        self.update_scoreboard()