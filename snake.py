from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:

    
    def __init__(self):
        self.segments = []
        self.createSnake()
        
    def createSnake(self):
        for postion in STARTING_POSITION:
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(postion)
            self.segments.append(segment)
    
    
    def move(self):
        for segNum in range(len(self.segments)-1, 0, -1):
            newX = self.segments[segNum-1].xcor()
            newY = self.segments[segNum-1].ycor()
            self.segments[segNum].goto(newX, newY)
        self.segments[0].forward(MOVE_DISTANCE)    