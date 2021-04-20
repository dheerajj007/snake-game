from turtle import Turtle, Screen
from snake import Snake
from scoreboard import ScoreBoard
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreBoard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
    
gameIsOn = True 

while gameIsOn:
    screen.update()
    time.sleep(0.1)
    snake.move()   
    
    #to update score as snake eats food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreBoard.increaseScore()
        snake.extend()
        
    #to detect collision with walls
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        gameIsOn = False
        scoreBoard.gameOver()
                
    #to detect collision with its tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            gameIsOn = False
            scoreBoard.gameOver()

screen.exitonclick()