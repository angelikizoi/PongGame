from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score, Line
import time

# Setup screen
screen = Screen()
screen.bgcolor("black")  # Background color
screen.setup(1000, 600)  # Window size
screen.title("Pong")  # Title of the game
screen.tracer(0)  # Turn off automatic screen updates for smoother animation

# Create game objects
paddle1 = Paddle(-460)  # Left paddle
paddle2 = Paddle(460)  # Right paddle
ball = Ball()  # Ball object
score1 = Score(-40)  # Score for the left player
score2 = Score(40)  # Score for the right player
line = Line()  # Middle line on the screen

# Paddle controls
screen.listen()  # Listen for key presses
screen.onkeypress(paddle1.up, "A")  # Left paddle up
screen.onkeypress(paddle1.down, "Z")  # Left paddle down
screen.onkeypress(paddle2.up, "Up")  # Right paddle up
screen.onkeypress(paddle2.down, "Down")  # Right paddle down

# Main game loop
game_on = True
while game_on:
    ball.move(paddle1, paddle2)  # Move the ball
    screen.update()  # Refresh the screen
    time.sleep(ball.time_move)  # Control ball speed
    # If the ball crosses the right boundary, left player scores
    if ball.xcor() > 480:
        score1.score_add()
        ball.ball_home()
    # If the ball crosses the left boundary, right player scores
    elif ball.xcor() < -480:
        score2.score_add()
        ball.ball_home()

# Close the game window on click
screen.exitonclick()
