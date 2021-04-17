from turtle import Turtle
FONT = ("Arial", 20, "normal")
ALIGNMENT = "center"

class ScoreBoard(Turtle):
        
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.updateScoreBoard()
        self.hideturtle()
        
    def updateScoreBoard(self):
        self.write(f"Score: {self.score}", font=FONT, align=ALIGNMENT)
        
    def increaseScore(self):
        self.score += 1
        self.clear()
        self.updateScoreBoard()
        
    def gameOver(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", font=FONT, align=ALIGNMENT)
        