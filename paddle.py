from turtle import Turtle

# Constants for paddle directions
UP = 90
DOWN = 270

# Paddle class inherits from Turtle
class Paddle(Turtle):
    def __init__(self, xcor):
        super().__init__()
        self.shape("square")  # Paddle shape
        self.color("white")  # Paddle color
        self.shapesize(4, 1)  # Paddle size (length, width)
        self.speed("fastest")  # Paddle speed
        self.penup()  # No drawing while moving
        self.xcor = xcor  # Horizontal position of the paddle
        self.goto(xcor, 0)  # Place the paddle at the initial position

    # Move the paddle up
    def up(self):
        new_y = self.ycor() + 30  # Calculate new position
        self.goto(self.xcor, new_y)  # Move paddle

    # Move the paddle down
    def down(self):
        new_y = self.ycor() - 30  # Calculate new position
        self.goto(self.xcor, new_y)  # Move paddle
