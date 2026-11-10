from turtle import Screen
from paddle import Paddle
from score_board import ScoreBoard
from pong_screen import PongScreen
from ball import Ball
import time
#constants fro screen proportions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
#Initialize screen
screen = Screen()
screen.setup(SCREEN_WIDTH,SCREEN_HEIGHT)
screen.bgcolor('black')
screen.tracer(0)
screen.title('Pong')
game_on = True
#initialize screen listening and creating paddle instances
screen.listen()
paddle_player_1 = Paddle(1)
paddle_player_2 = Paddle(2)
ball = Ball()
#add event listeners
screen.onkeypress(key='w',fun=paddle_player_2.move_up)
screen.onkeypress(key='s',fun=paddle_player_2.move_down)
screen.onkeypress(key='Up',fun=paddle_player_1.move_up)
screen.onkeypress(key='Down',fun=paddle_player_1.move_down)
#game loop
pong_screen = PongScreen() 
score_board = ScoreBoard()
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        #bounce
        ball.bounce_y()
    #detect collision with right paddle
    if ball.distance(paddle_player_1.paddle_segments[1]) < 70 and ball.xcor() > 240 or ball.distance(paddle_player_2.paddle_segments[1]) < 70 and ball.xcor() < -240:
        ball.bounce_x()
    if ball.xcor() > 290:
        score_board.update_score(2)
        ball.inc_speed()
        ball.refresh()
    elif ball.xcor() < -290:
        score_board.update_score(1)
        ball.inc_speed()
        ball.refresh()

    



screen.exitonclick()