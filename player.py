from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.left(90)
        self.color("Black")
        self.penup()
        self.goto_start()

    def move(self):
        self.forward(MOVE_DISTANCE)
    def goto_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finishline(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
