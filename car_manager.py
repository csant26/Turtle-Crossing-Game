"""Setting up the car manager"""

import turtle
import random
import constants as cons

class Car(turtle.Turtle):
    """Car"""
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=3,stretch_wid=1)
        self.color(random.choice(cons.CAR_COLORS))
        self.setheading(180)


class CarManager():
    """Cars manager"""
    def __init__(self):
        self.cars:list[Car] = []
        self.create_multiple_cars()
        self.dx = 1

    def create_single_car(self):
        """"Create a single car."""
        my_car = Car()

        while True:
            x = random.randint(cons.CAR_MIN_XCOOR, cons.CAR_MAX_XCOOR)
            y = random.randint(cons.CAR_MIN_YCOOR, cons.CAR_MAX_YCOOR)

            if self.is_position_free(x, y):
                my_car.goto(x, y)
                self.cars.append(my_car)
                break

    def create_multiple_cars(self):
        """Create cars"""
        for _ in range(1,70):
            self.create_single_car()

    def is_position_free(self, x, y):
        """Decides if a particular coordinate is free to place car"""
        for car in self.cars:
            same_lane = abs(car.ycor() - y) < 20
            too_close_x = abs(car.xcor() - x) < 90

            if same_lane and too_close_x:
                return False
        return True

    def move_cars(self):
        """Move cars"""
        for car in self.cars:
            next_x = car.xcor() - self.dx
            if next_x < cons.CAR_MIN_XCOOR:
                next_x = cons.CAR_MAX_XCOOR
            car.goto(next_x,car.ycor())

    def increase_car_pace(self):
        """Increase car pace each level"""
        self.dx += 0.5
