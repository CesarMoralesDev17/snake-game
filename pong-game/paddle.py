from turtle import Turtle
STARTING_POSITIONS_P1 = [(250,20),(250,0),(250,-20)]
STARTING_POSITIONS_P2 = [(-250,20),(-250,0),(-250,-20)] 
STEP = 20
TOP = 250
BOTTOM = -250
class Paddle():
    def __init__(self,player):
        self.paddle_segments = []
        self.player = player
        self.create_paddle(self.player)
        self.head = self.paddle_segments[0]
        self.tail = self.paddle_segments[1]
        self.head.seth(90)
        self.tail.seth(270)
        
    def create_paddle(self,player):
        if player == 1:
            for coordinate in STARTING_POSITIONS_P1:
                segment = Turtle()
                segment.shape('square')
                segment.color('white')
                segment.penup()
                segment.goto(coordinate)
                self.paddle_segments.append(segment)
        if player == 2:
            for coordinate in STARTING_POSITIONS_P2:
                segment = Turtle()
                segment.shape('square')
                segment.color('white')
                segment.penup()
                segment.goto(coordinate)
                self.paddle_segments.append(segment)
    def move_up(self):
        if self.paddle_segments[0].ycor() < TOP:
            for segment in self.paddle_segments:
                x_cor = segment.xcor()
                y_cor = segment.ycor()
                segment.goto(x_cor,y_cor+20)
    def move_down(self):
        if self.paddle_segments[2].ycor() > BOTTOM:
            for segment in self.paddle_segments:
                x_cor = segment.xcor()
                y_cor = segment.ycor()
                segment.goto(x_cor,y_cor-20)

                


        