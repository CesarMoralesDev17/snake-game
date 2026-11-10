from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier',22,'normal')
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as data:
            self.highscore = int(data.read())
        self.hideturtle()
        self.speed("fastest")
        self.goto(0,270)
        self.color("white")
        self.update_score()
    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score} Highscore: {self.highscore}",False,align = ALIGNMENT,font=FONT)
        return self.score
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.clear()
        self.write("GAME OVER",False,align = ALIGNMENT,font=FONT)

        