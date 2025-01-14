# Turtle Crossing Game

Welcome to the **Turtle Crossing Game**, a fun and engaging game built using Python's `turtle` graphics module. The goal of the game is to navigate the turtle safely across the road while avoiding moving cars.

## Features

- Player-controlled turtle that moves up and down.
- Randomly generated cars with varying colors and speeds.
- Incremental difficulty as the player progresses through levels.
- "Game Over" display when the turtle collides with a car.

## Game Rules

1. Use the **Up arrow key** to move the turtle forward.
2. Use the **Down arrow key** to move the turtle backward.
3. Avoid colliding with the cars.
4. Reach the top of the screen to advance to the next level.
5. Each level increases the speed of the cars.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/masood2004/turtle-crossing.git
   ```

2. Navigate to the project directory:
   ```bash
   cd turtle-crossing
   ```

3. Ensure you have Python installed on your system (Python 3.7 or later is recommended).

4. Install any required dependencies (if applicable).

## How to Play

1. Run the game script:
   ```bash
   python main.py
   ```

2. Use the arrow keys to control the turtle and avoid cars.
3. Try to reach the finish line (top of the screen) to level up.
4. The game ends when the turtle collides with a car.

## File Structure

```
.
├── main.py              # Main game script
├── player.py            # Player (turtle) class
├── car_manager.py       # CarManager class to handle car generation and movement
├── scoreboard.py        # Scoreboard class to track and display the level and game status
└── README.md            # Project documentation
```

## Classes Overview

### `Player`
- Represents the player-controlled turtle.
- Handles movement and resets the position after crossing the finish line.

### `CarManager`
- Manages the creation and movement of cars.
- Randomizes car positions and colors.
- Increases car speed as the player levels up.

### `Scoreboard`
- Displays the current level on the screen.
- Shows a "Game Over" message when the player loses.

## Contributing

Contributions are welcome! If you have ideas to improve the game or find any issues, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- Inspired by the classic arcade game "Frogger."
- Built using Python's `turtle` module.

---

Enjoy the game and have fun helping the turtle cross the road safely! 🐢🚗

