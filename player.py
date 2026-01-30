"""Setting up player module"""
import turtle
import constants as cons

class Player(turtle.Turtle):
    """Player"""
    def __init__(self):
        super().__init__()
        self.color(cons.PLAYER_COLOUR)
        self.penup()
        self.goto(x=cons.INITIAL_PLAYER_XCOOR,y=cons.INITIAL_PLAYER_YCOOR)
        self.shape("turtle")
        self.shapesize(stretch_len=0.8,stretch_wid=0.8)
        self.setheading(90)

    def move_player_up(self):
        """Moves player up""" 
        if self.ycor() < cons.PLAYER_MAX_YCOOR:
            self.forward(cons.PLAYER_PACE)

    def move_player_down(self):
        """Moves player down"""
        if self.ycor() > cons.PLAYER_MIN_YCOOR:
            self.backward(cons.PLAYER_PACE)

    def move_player_left(self):
        """Moves player left"""
        if self.xcor() > cons.PLAYER_MIN_XCOOR:
            self.goto(self.xcor()-cons.PLAYER_PACE,self.ycor())

    def move_player_right(self):
        """Moves player right"""
        if self.xcor() < cons.PLAYER_MAX_XCOOR:
            self.goto(self.xcor()+cons.PLAYER_PACE,self.ycor())

    def reset_player(self):
        """Resets player"""
        self.goto(x=cons.INITIAL_PLAYER_XCOOR,y=cons.INITIAL_PLAYER_YCOOR)
