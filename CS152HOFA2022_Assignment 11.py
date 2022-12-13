#Raymond Cheung
#Objects, inheritance, polymorphism intro
#Assignment 11 due 12/4/2022
# Draws several lines radiating out from the origin.
import turtle
import random

class StampTurtle(turtle.Turtle):
    # Constructor - just copy and use for now
    # Step 2, 3, 4,5 | created custom forward and backward method for stamp turtles
    def __init__(self):
        super().__init__()

    def forward(self, dist):
        super().forward(dist)
        self.stamp()

    def backward(self, dist):
        super().backward(dist)
        self.stamp()
        self.color(random.choice(['red', 'green', 'blue', 'yellow','pink', 'black']))

class MorphingTurtle(turtle.Turtle):
    # Constructor - just copy and use for now
    # Step 6 | Construct Morphing Turtle object that has different forwards and backwards functions (described below)
    def __init__(self):
        super().__init__()

    def forward(self, dist):
        #new forward function that goes forward and stamps a random list of shapes at a random size, to create shape trail
        self.penup()
        self.shape(random.choice(['arrow', 'classic', 'turtle','circle', 'square']))
        self.turtlesize(random.random())
        self.stamp()
        super().forward(dist)

    def backward(self, dist):
        #new backward function that changes color, shape, speed, pen and turtle size | leaving a random colored/shaped line track
        self.speed(0)
        self.color(random.choice(['gold', 'tomato', 'skyblue', 'orange', 'purple']))
        self.shape(random.choice(['arrow', 'classic', 'turtle','circle', 'square']))
        self.turtlesize(0.5)
        self.pensize(0.75)
        super().backward(dist)
        self.stamp()


def main():
    # named constants
    screen_size = 500
    screen_startx = 60  # x coordinate of the left edge of the graphics window
    # Set up the window and its attributes
    wn = turtle.Screen()
    wn.setup(screen_size, screen_size, screen_startx, 0)
    turtle_list = []
    num_turtles = 2
    num_stamp_turtles = 3
    num_morphing_turtles = 3
    # Create a list of different colored turtles, each pointing
    #   in a different direction
    for _ in range(num_turtles):
        t = turtle.Turtle()
        t.right(random.randrange(350))
        t.color(random.choice(['red', 'green', 'blue', 'yellow']))
        # t.speed(7)
        turtle_list.append(t)

    # Create a list of different colored stamp_turtles, each pointing
    #   in a different direction

    for _ in range(num_stamp_turtles):
        #Step 1 | Uncomment stamp turtle object creator
        t = StampTurtle()
        t.right(random.randrange(350))
        t.color('black')
        #t.speed(7)
        turtle_list.append(t)

    for _ in range(num_morphing_turtles):
        #creates X number specified of morphingTurtle object and appends it to the turtle list, colored red to show difference when intializing
        t = MorphingTurtle()
        t.right(random.randrange(350))
        t.color('red')
        turtle_list.append(t)

    # Move each turtle outward from the origin ten times
    for t in turtle_list:
        #test function of different turtle objects performing unique backward and forward methods
        for _ in range(10):
            t.backward(random.randrange(10, 30))





    wn.exitonclick()


# Run the main function. This should be the last statement in the file.
main()