from turtle import Screen
import time
from snakes import Snakes
from food import Food
from scoreboard import Score

screen = Screen()
screen.tracer(0)
screen.bgcolor("dim grey")
screen.title(" My Snake Game ")
screen.setup(width=600, height=600)

snake = Snakes()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
food = Food()
score = Score()
is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # Detect collision with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset_game()
        snake.reset()

    # Detect collision with the tail
    for segments in snake.snake_segments[1:]:
        if snake.head.distance(segments) < 10:
            score.reset_game()
            snake.reset()

screen.exitonclick()
