from turtle import Turtle
BOTTOM_CORDS = (0,-300)
STEP = 25

class PongScreen(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(BOTTOM_CORDS)
        self.color('white')
        self.seth(90)
        for i in range(0,13):
            self.pendown()
            self.forward(STEP)
            self.penup()
            self.forward(STEP)
