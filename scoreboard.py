FONT = ("Courier", 24, "normal")

from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 250)
        self.color('white')
        self.write(f'Score: {self.score}', align='center', font=FONT)
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score}', align='center', font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align='center', font=FONT)