from turtle import Turtle  # Import the Turtle class for creating the player object

# Constants for player attributes and movement
# The starting position of the player (bottom center of the screen)
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10  # Distance the player moves with each step
FINISH_LINE_Y = 280  # Y-coordinate of the finish line (top of the screen)


class Player(Turtle):
    """
    A class to represent the player in the Turtle Crossing Game.
    The player is controlled to move up and down the screen to avoid obstacles and reach the finish line.
    """

    def __init__(self):
        """
        Initializes the Player object with a turtle shape, starting position, and orientation.
        """
        super().__init__()  # Initialize the parent Turtle class
        self.shape("turtle")  # Set the shape of the player to a turtle
        self.left(90)  # Rotate the player to face upward
        self.penup()  # Lift the pen to prevent drawing lines
        # Move the player to the starting position
        self.goto(STARTING_POSITION)

    def move_up(self):
        """
        Moves the player upward by a fixed distance.
        Called when the "Up" key is pressed.
        """
        self.forward(
            MOVE_DISTANCE)  # Move forward in the direction the player is facing

    def move_down(self):
        """
        Moves the player downward by a fixed distance.
        Called when the "Down" key is pressed.
        """
        self.backward(
            MOVE_DISTANCE)  # Move backward in the direction the player is facing

    def from_start(self):
        """
        Resets the player's position to the starting point.
        Called when the player successfully crosses the screen or when the game resets.
        """
        self.goto(
            STARTING_POSITION)  # Move the player back to the starting position
