from turtle import Turtle
ALIGN="center"
FONT=("Courier",13,"normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.hideturtle()  # to hide the turtle that shows up
        self.penup()
        self.goto(0,270)
        self.write(f"Score:{self.score}",align=ALIGN,font=FONT)
    def increase_score(self):
        self.score+=1
        self.clear()
        self.write(f"Score:{self.score}", align=ALIGN,font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 200)
        self.write(f"Game over!\nFinal score: {self.score}\n", align=ALIGN,font=FONT)
