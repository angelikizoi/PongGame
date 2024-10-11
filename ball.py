from turtle import Turtle
import random

# Ball class inherits from Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")  # Shape of the ball
        self.penup()  # No drawing while moving
        self.color("white")  # Ball color
        self.shapesize(0.5, 0.5)  # Ball size
        self.speed("fastest")  # Speed of the ball
        self.time_move = 0.1  # Initial delay between moves
        self.ball_home()  # Start ball in random direction

    # Reset the ball to the center and choose a random initial direction
    def ball_home(self):
        self.home()  # Go to center (0, 0)
        self.time_move = 0.1  # Reset speed
        rand_range = [random.randint(0, 70), random.randint(110, 250), random.randint(290, 360)]  # Random angles
        self.setheading(random.choice(rand_range))  # Set the ball's direction

    # Move the ball, check for collision with walls and paddles
    def move(self, p1, p2):
        self.forward(15)  # Move ball forward
        new_heading = 360 - self.heading()  # Reflect off top/bottom walls
        # Check for collision with top or bottom of the screen
        if self.ycor() > 280 or self.ycor() < -280:
            self.setheading(new_heading)
            self.forward(15)
        # Check for collision with paddles
        elif (self.distance(p1) < 40 or self.distance(p2) < 40) and (self.xcor() > 450 or self.xcor() < -450):
            new_heading = 180 - self.heading()  # Reflect off the paddle
            self.time_move *= 0.9  # Increase ball speed
            self.setheading(new_heading)
            self.forward(15)
