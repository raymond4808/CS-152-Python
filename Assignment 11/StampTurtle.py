
# Draws several lines radiating out from the origin. 
import turtle
import random
class StampTurtle(turtle.Turtle):
    # Constructor - just copy and use for now
    def __init__(self):
        super().__init__()
        
        
def main():
    # named constants
    screen_size = 500
    screen_startx = 60 # x coordinate of the left edge of the graphics window
    # Set up the window and its attributes
    wn = turtle.Screen()              
    wn.setup(screen_size, screen_size, screen_startx, 0)
    turtle_list = []
    num_turtles = 2
    num_stamp_turtles = 3
    # Create a list of different colored turtles, each pointing
    #   in a different direction
    for _ in range(num_turtles):
        t = turtle.Turtle()
        t.right(random.randrange(350))
        t.color(random.choice(['red','green','blue','yellow']))
        #t.speed(7)
        turtle_list.append(t)
    
    # Create a list of different colored stamp_turtles, each pointing
    #   in a different direction
    '''
    for _ in range(num_stamp_turtles):
        t = StampTurtle()
        t.right(random.randrange(350))
        t.color('black')
        #t.speed(7)     
        turtle_list.append(t)
    '''
    
    # Move each turtle outward from the origin ten times
    for t in turtle_list:
        for _ in range(10):
            t.forward(random.randrange(10,30))
    wn.exitonclick()
# Run the main function. This should be the last statement in the file.
main()