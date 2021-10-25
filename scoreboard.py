from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.texthere()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"Score: {self.score}", align="center", font=("courier", 15, "normal"))

    def game_over(self):
        self.penup()
        self.goto(0,0)
        self.write(arg="Game Over", align="center", font=("courier", 18, "normal"))
        self.color("green")



    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()

        self.color("white")


    def texthere(self):
        self.goto(x=0, y=276)
        self.hideturtle()
        self.score = 0












