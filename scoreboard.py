from turtle import Turtle  # Import the Turtle class for creating the scoreboard

# Define the font style for the scoreboard text
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """
    A class to create and manage the scoreboard for the Turtle Crossing Game.
    Inherits from the Turtle class for text display functionality.
    """

    def __init__(self, shape="classic", undobuffersize=1000, visible=True):
        """
        Initializes the Scoreboard object with default or specified attributes.
        Sets the initial level to 1 and displays the initial score.

        Parameters:
        - shape (str): The shape of the Turtle (default is "classic").
        - undobuffersize (int): Buffer size for undo actions (default is 1000).
        - visible (bool): Whether the Turtle is visible upon creation (default is True).
        """
        super().__init__(shape, undobuffersize, visible)  # Initialize parent class
        self.level = 1  # Start the game at level 1
        self.update_score()  # Display the initial score on the screen

    def update_score(self):
        """
        Updates the scoreboard to display the current level.
        Clears any previous text and writes the updated score.
        """
        self.hideturtle()  # Hide the Turtle to display only the text
        self.penup()  # Lift the pen to prevent drawing lines
        self.goto(-200, 250)  # Position the scoreboard at the top-left corner
        self.write(f"Level: {self.level}", align="center",
                   font=(FONT))  # Display the current level

    def increment_level(self):
        """
        Increments the level by 1 and updates the scoreboard.
        Clears the previous level display and writes the new level.
        """
        self.level += 1  # Increase the level by 1
        self.reset()  # Clear the Turtle's drawings and reset its state
        self.update_score()  # Update the scoreboard with the new level

    def game_over(self):
        """
        Displays the "Game Over" message in the center of the screen.
        Called when the game ends due to a collision.
        """
        self.goto(0, 0)  # Move to the center of the screen
        # Display the "Game Over" message
        self.write("Game Over.", align="center", font=(FONT))
