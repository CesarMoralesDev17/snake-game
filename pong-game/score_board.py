from turtle import Turtle
BOTTOM_CORDS = (0,-300)
STEP = 25
PLAYER_1_TYPING_COORDS = (100,260)
PLAYER_2_TYPING_COORDS = (-100,260)
TYPING_COORDS = [PLAYER_1_TYPING_COORDS,PLAYER_2_TYPING_COORDS]
FONT = ('Courier',20,'normal')
ALIGNMENT = 'center'
MOVE = False
class ScoreBoard():
    def __init__(self):
        self.score_p1 = 0
        self.score_p2 = 0
        self.scores = [self.score_p1,self.score_p2]
        self.boards = []
        for i in range (0,2):
            new_board = Turtle()
            new_board.hideturtle()
            new_board.penup()
            new_board.color('white')
            new_board.goto(TYPING_COORDS[i])
            self.boards.append(new_board)
        self.show_scores()
    
    def show_scores(self):
        for i in range(0,2):
            self.boards[i].clear()
            self.boards[i].write(f"{self.scores[i]}",MOVE,ALIGNMENT,FONT)
    def update_score(self,p):
        if p == 1:
            self.scores[0] += 1
        if p == 2:
            self.scores[1] += 1
        self.show_scores()








