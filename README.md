
# Pong Game - Python Turtle Version

This is a simple Pong game built using Python's Turtle Graphics library. Two players can control paddles to bounce a ball back and forth. The first player to miss the ball loses, and the opponent gains a point. The game is simple, fun, and perfect for demonstrating basic Python graphics and game development concepts.

## Features
- Two-player game with paddles and a bouncing ball.
- The ball speeds up each time it hits a paddle.
- The game displays the current score of both players.

## Requirements

- Python 3.x
- `turtle` module (comes pre-installed with Python)
- `random` module (comes pre-installed with Python)

## Installation

### Step 1: Clone the repository

```bash
git clone https://github.com/angelikizoi/PongGame.git
cd PongGame
```

### Step 2: Create a virtual environment (optional but recommended)

On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

On macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install dependencies

No external dependencies are needed besides the standard Python libraries.

### Step 4: Run the game

```bash
python main.py
```

## How to Play

- Player 1 (left paddle) controls:  
  - Move up: Press the 'A' key  
  - Move down: Press the 'Z' key  
  
- Player 2 (right paddle) controls:  
  - Move up: Press the 'Up Arrow' key  
  - Move down: Press the 'Down Arrow' key

## Game Logic

- The ball bounces off the top and bottom walls.
- The ball bounces off the paddles, increasing its speed each time.
- If the ball passes a paddle, the opponent scores a point.
- The game keeps track of each player's score.

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute this project.

