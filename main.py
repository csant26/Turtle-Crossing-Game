"""Main module for Turtle Cross"""
import turtle
import tkinter.messagebox as msg
import constants as cons
import scoreboard
import player
import car_manager

class TurtleCross:
    """TurtleCross"""
    def __init__(self):
        self.initialize_screen()
        self.initialize_player()
        self.record_player_name()
        self.initialize_player_motion()
        self.initialize_car_manager()
        self.initialize_scoreboard()
        self.game_on = True

    def initialize_screen(self):
        """Initialize Pong screen"""
        self.screen = turtle.Screen()
        self.screen.setup(width=cons.SCREEN_WIDTH,height=cons.SCREEN_HEIGHT)
        self.screen.bgcolor(cons.SCREEN_BACKGROUND_COLOR)
        self.screen.title("Turtle Cross")
        self.screen.tracer(0)

    def initialize_scoreboard(self):
        """Initialize scoreboard"""
        self.score = scoreboard.Scoreboard()

    def initialize_player(self):
        """Initialize player"""
        self.player = player.Player()

    def initialize_car_manager(self):
        """Initialize car manager"""
        self.car_manager = car_manager.CarManager()

    def initialize_player_motion(self):
        """Enables player motion"""
        self.screen.listen()
        # self.screen.onkey(self.player.move_player,"Up")
        self.screen.onkeypress(self.player.move_player_up,"Up")
        self.screen.onkeypress(self.player.move_player_down,"Down")
        self.screen.onkeypress(self.player.move_player_right,"Right")
        self.screen.onkeypress(self.player.move_player_left,"Left")

    def record_player_name(self):
        """Records player name"""
        self.player_name = self.screen.textinput("Welcome to Crossing Game",
                                                 "May I have your name please?")
        self.screen.title(f"You can do it! {self.player_name}")

    def has_collided(self, plyr:player.Player, car:car_manager.Car):
        """Determines if player has collided with car"""
        dx = abs(plyr.xcor() - car.xcor())
        dy = abs(plyr.ycor() - car.ycor())

        car_half_width = 30   # 60 / 2
        car_half_height = 10  # 20 / 2

        player_half_length = 18
        player_half_width = 11

        return (
            dx < car_half_width + player_half_length and
            dy < car_half_height + player_half_width
        )

    def game_loop(self):
        """Runs game on loop"""
        if not self.game_on:
            self.screen.bye()
            return

        # Move the cars here.
        self.car_manager.move_cars()

        if self.player.ycor() > cons.PLAYER_MAX_YCOOR - 30:
            self.player.reset_player()
            self.score.update_scoreboard()

        for car in self.car_manager.cars:
            if self.has_collided(self.player,car):
                msg.showerror("LOST","Nice try. But, you've lost.")
                self.game_on = False

        self.screen.update()
        self.screen.ontimer(self.game_loop,16)


    def run(self):
        """Starts game."""   
        self.game_loop()
        self.screen.mainloop()

turtle_cross = TurtleCross()
turtle_cross.run()
