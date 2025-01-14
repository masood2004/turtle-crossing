# Import necessary modules
import time
from turtle import Screen
from player import Player  # Import the Player class from player module
# Import the CarManager class from car_manager module
from car_manager import CarManager
# Import the Scoreboard class from scoreboard module
from scoreboard import Scoreboard

# Setup the screen for the game
screen = Screen()
screen.setup(width=600, height=600)  # Set the screen dimensions
screen.tracer(0)  # Turn off automatic screen updates for smoother animation
screen.title("Turtle Crossing Game")  # Set the window title

# Initialize game components
player = Player()  # Create the player object
car_manager = CarManager()  # Create the car manager object
scoreboard = Scoreboard()  # Create the scoreboard object

# Set up key listeners for player movement
screen.listen()  # Enable the screen to listen for keyboard inputs
# Move the player up when "Up" key is pressed
screen.onkeypress(fun=player.move_up, key="Up")
# Move the player down when "Down" key is pressed
screen.onkeypress(fun=player.move_down, key="Down")

# Game loop control variable
game_is_on = True

# Start the main game loop
while game_is_on:
    time.sleep(0.1)  # Pause for a short duration to control the game's speed
    screen.update()  # Update the screen to reflect the latest changes

    # Create new cars at random intervals
    car_manager.create_cars()

    # Move all the cars across the screen
    car_manager.move_cars()

    # Check for collision between player and any car
    for car in car_manager.all_cars:
        # If the car is too close to the player, end the game
        if car.distance(player) < 20:  # Collision detection based on distance
            game_is_on = False  # Stop the game loop
            scoreboard.game_over()  # Display the "Game Over" message

    # Check if the player has successfully crossed to the other side
    if player.ycor() > 290:  # If the player's y-coordinate exceeds 290
        scoreboard.increment_level()  # Increase the player's level
        player.from_start()  # Reset the player's position to the starting point
        car_manager.increase_speed()  # Increase the speed of the cars for added difficulty

# Exit the game when the user clicks on the screen
screen.exitonclick()
