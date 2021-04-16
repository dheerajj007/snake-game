from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
    
gameIsOn = True 

while gameIsOn:
    screen.update()
    time.sleep(0.1)
    snake.move()    


screen.exitonclick()