from turtle import Turtle
ORIGINAL_POS = [0,0]
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
    def add_segment(self,position):
        snake_segment = Turtle()
        snake_segment.penup()
        snake_segment.color('white')
        snake_segment.shape('square')
        snake_segment.goto(position)
        self.snake_segments.append(snake_segment)

    def move(self):
        for seg_num in range(len(self.snake_segments)-1,0,-1):
            new_x = self.snake_segments[seg_num-1].xcor()   
            new_y = self.snake_segments[seg_num-1].ycor()
            self.snake_segments[seg_num].goto(new_x,new_y)    
        self.head.forward(MOVE_DISTANCE)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)
    def down(self):
        if self.head.heading() != UP:   
            self.head.seth(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def extend(self):
        #add new segment
        self.add_segment(self.snake_segments[-1].position())