from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP=90
DOWN=270
RIGHT=180
LEFT=0
class Snake:
    
    def __init__(self):
        self.segments = []
        self.createSnake()
        self.head = self.segments[0]    
        
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
        self.head.forward(MOVE_DISTANCE)    
        
    def up(self):  
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)