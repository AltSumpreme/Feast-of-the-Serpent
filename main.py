from turtle import Screen, onkey
from snake_mech import Snake
from Snake_food import Food
import time
from snake_scorecard import Scorecard

scorecard=Scorecard()
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Feast of the Serpent')
screen.tracer(0)
food=Food()
snake = Snake()
game_is_on = True

screen.listen()
onkey(snake.up, "Up")
onkey(snake.down, "Down")
onkey(snake.left, "Left")
onkey(snake.right, "Right")

while game_is_on:
    screen.update()
    snake.move()
    time.sleep(0.1)
    if snake.head.distance(food)<15:
       food.refresh()
       scorecard.increase_score()
    for segs in snake.segments[1:]:
            
            if snake.head.distance(segs)<10:
                game_is_on=False
                scorecard.gameover()
            if snake.head.xcor()>300 or snake.head.xcor()<- 300 or snake.head.ycor()>300 or snake.head.ycor()<-300:
                game_is_on = False
                scorecard.gameover()
       
       
   

screen.exitonclick()
