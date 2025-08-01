from turtle import Screen
from snake import Snake
from food import  Food
from scoreboard import ScoreBoard
import time
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("~ Friends Game ~")
screen.tracer(0)
# screen.register_shape("snake", ((0,0), (60,0), (60,20),(20,0)))
# screen.register_shape("square", ((-10,-30), (-10,30), (10,30),(10,-30)))
snake = Snake()
food  = Food()
scoreboard = ScoreBoard()
screen.listen()

screen.onkey(key="Up",fun=snake.up)
screen.onkey(key="Down",fun=snake.down)
screen.onkey(key="Left",fun=snake.left)
screen.onkey(key="Right",fun=snake.right)

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.20)
    snake.move()

    # Detect Food.
    if snake.head.distance(food) < 15:
        food.refresh_food()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with wall.
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 280 or snake.head.ycor() < -290:
        is_game_on = False
        scoreboard.game_over()

    #Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over()










screen.exitonclick()