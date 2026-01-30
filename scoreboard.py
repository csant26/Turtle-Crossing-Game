"""Setting up the Scoreboard"""
import turtle
import constants as cons

class Scoreboard(turtle.Turtle):
    """Scoreboard"""
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level_count = 0
        self.goto(x=cons.SCORE_XCOOR,y=cons.SCORE_YCOOR)
        self.color(cons.SCORE_COLOUR)
        self.update_scoreboard()

    def update_scoreboard(self):
        """Updates levels"""
        self.level_count += 1
        self.clear()
        self.write(f"Level {self.level_count}",font=("Courier",30,"bold"))

