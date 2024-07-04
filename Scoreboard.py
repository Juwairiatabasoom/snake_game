from turtle import Turtle
ALIGN="center"
FONT=("Courier",13,"normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.highscore=0
        self.hideturtle()  # to hide the turtle that shows up
        self.penup()
        self.goto(0,270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score}  HighScore:{self.highscore}",align=ALIGN,font=FONT)

    def refresh(self):
        if self.score>self.highscore:
            self.highscore = self.score
            self.score=0
            self.update_scoreboard()


    def increase_score(self):
        self.score+=1
        self.update_scoreboard()

