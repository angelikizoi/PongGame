from turtle import Turtle

# Class to create the center line on the screen
class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()  # Hide turtle
        self.pencolor("white")  # Line color
        self.pensize(6)  # Line thickness
        self.penup()
        self.goto(0, 300)  # Start drawing from top middle
        self.setheading(270)  # Set direction to move downwards
        # Draw the dashed line in the middle
        for i in range(20):
            self.pendown()
            self.fd(20)  # Draw part of the line
            self.penup()
            self.fd(20)  # Skip part of the line

# Class to handle player score
class Score(Turtle):
    def __init__(self, paddle):
        super().__init__()
        self.score = 0  # Initialize score
        self.ht()  # Hide turtle
        self.penup()
        self.pencolor("white")  # Score color
        self.paddle = paddle  # Position of the score (left or right)
        self.score_on_board()  # Display initial score

    # Display the current score on the screen
    def score_on_board(self):
        self.goto(self.paddle, 230)  # Position the score
        self.write(f"{self.score}", True, "center", ('Kristen ITC', 50, 'bold'))  # Display score

    # Update the score and refresh it on the screen
    def score_add(self):
        self.score += 1  # Increment score
        self.clear()  # Clear the previous score
        self.score_on_board()  # Display updated score
