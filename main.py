from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My_Snake_Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkeypress(snake.Up, "Up")
screen.onkeypress(snake.Down, "Down")
screen.onkeypress(snake.Left, "Left")
screen.onkeypress(snake.Right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

#     detect collisions with the food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

#     detect collision wih the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()

#     detect collision with the tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()
