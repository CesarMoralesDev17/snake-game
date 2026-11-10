from turtle import Screen
from snake import Snake
from food import Food
from score import ScoreBoard
import time
WALL_NEG = -280
WALL_POS = 280
screen = Screen()
screen.bgcolor('black')
screen.setup(width=600,height=600)
screen.title(titlestring="Snake game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = ScoreBoard()
screen.update()
screen.listen()
screen.onkey(key = 'Up',fun = snake.up)
screen.onkey(key = 'Down',fun= snake.down)
screen.onkey(key = 'Left',fun= snake.left)
screen.onkey(key = 'Right',fun = snake.right)
game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
#Detect collision with food
    if snake.head.distance(food) < 15:
        
        food.refresh()
        snake.extend()
        scoreboard.update_score()
#Detect collision with wall
    if snake.head.xcor() < WALL_NEG or snake.head.xcor() > WALL_POS or snake.head.ycor() < WALL_NEG or snake.head.ycor() > WALL_POS:
        scoreboard.reset()
        game_on = False
#Detect collision with tail
    for segment in snake.snake_segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            game_on = False
        












screen.exitonclick()