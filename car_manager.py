from turtle import Turtle  # Import the Turtle class to create car objects
import random  # Import random module to generate random positions and attributes

# Constants for car attributes and movement
COLORS = ["red", "orange", "yellow", "green",
          "blue", "purple"]  # List of car colors
STARTING_MOVE_DISTANCE = 5  # Initial speed of the cars
MOVE_INCREMENT = 10  # Speed increment when the player levels up


class CarManager(Turtle):
    """
    A class to manage the creation and movement of cars in the Turtle Crossing Game.
    Inherits from the Turtle class for object creation and manipulation.
    """

    def __init__(self):
        """
        Initializes the CarManager object.
        Sets up an empty list to store car objects and defines the initial car speed.
        """
        super().__init__()  # Initialize the parent Turtle class
        self.hideturtle()  # Hide the Turtle object (used only as a base manager)
        self.all_cars = []  # List to store all car objects
        self.car_speed = STARTING_MOVE_DISTANCE  # Set the initial car speed

    def create_cars(self):
        """
        Creates a new car with a 1-in-6 chance on each game loop iteration.
        Randomly sets the car's position and color, then adds it to the list of cars.
        """
        random_num = random.randint(
            1, 6)  # Generate a random number between 1 and 6
        # Only create a car if the random number is 1 (1-in-6 chance)
        if random_num == 1:
            # Create a new Turtle object with a square shape
            new_car = Turtle("square")
            # Stretch the car to a rectangular shape
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()  # Lift the pen to avoid drawing lines
            # Assign a random color to the car
            new_car.color(random.choice(COLORS))
            # Generate a random y-coordinate within screen bounds
            random_y = random.randint(-250, 250)
            # Position the car at the far-right edge of the screen
            new_car.goto(300, random_y)
            # Add the new car to the list of all cars
            self.all_cars.append(new_car)

    def move_cars(self):
        """
        Moves all cars in the list to the left by the current speed value.
        Simulates cars driving across the screen.
        """
        for car in self.all_cars:  # Iterate through each car in the list
            # Move the car left by the current speed value
            car.backward(self.car_speed)

    def increase_speed(self):
        """
        Increases the speed of the cars by a predefined increment.
        Called when the player advances to the next level.
        """
        self.car_speed += MOVE_INCREMENT  # Increment the car speed for added difficulty
