from turtle import Turtle,Screen
import time
from snake import Snake
from food import Food
from Scoreboard import Scoreboard
screen=Screen()
screen.setup(600,600)
screen.bgcolor("CornflowerBlue")
screen.title("Snake Game")
screen.tracer(0)



snake=Snake()
food=Food()
scoreboard=Scoreboard()


screen.listen()

screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # detecting collision with food
    if snake.head.distance(food) < 15:
        food.refresh_food()
        scoreboard.increase_score()
        snake.extend()

    #detect collision with wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_is_on=False
        scoreboard.game_over()

    #detect collision with its tail:
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            game_is_on=False
            scoreboard.game_over()


screen.exitonclick()