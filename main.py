from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

def moveForward():
    timmy.forward(10)
def moveBackward():
    timmy.backward(10)
def moveLeft():
    timmy.setheading(timmy.heading() + 10)
    timmy.forward(10)
def moveRight():
    timmy.setheading(timmy.heading() - 10)
    timmy.forward(10)
def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()
    
screen.listen()
screen.onkey(moveForward, "w")
screen.onkey(moveBackward, "s")
screen.onkey(moveLeft, "a")
screen.onkey(moveRight, "d")
screen.onkey(clear, "c")
screen.exitonclick()