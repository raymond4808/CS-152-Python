# Draws 3 sets of shapes of related sizes
#   Draw a rectangle
#   Draw a triangle with sides the same size as rectangle length
#   Draw a filled circle with the same area as the rectangle
#   Draw a triangle with the same area as the rectangle
#   Draw a filled circle with the same diameter as the previous triangle side
#Assignment 6 
#10/16/2022
#Raymond Cheung

import turtle
import math

def next_y_position(y,ht):
    """ Returns the next y-position, given current position y and height ht """
    next = y + ht + 30
    return next

def drawRect(t, len, wid):
    """ Draws a rectangle using turtle t with sides len and wid """
    for side in [len, wid, len, wid]:
        t.forward(side)
        t.left(90)
        
def getSide(len,wid):
    """Returns the length of a triangle side with an area of len * wid  (Question 3)""" 
    sideTriangle = math.sqrt(len*wid*4/math.sqrt(3))
    return sideTriangle

def getRad(len,wid):                
    """ Returns the radius of a circle with an area of len * wid (Question 4) """  
    radiusCircle= math.sqrt(len*wid/math.pi)
    return radiusCircle

def drawFillCircle (turtle, rad):
# Question 1
    turtle.begin_fill()
    turtle.circle(rad)
    turtle.end_fill()

def drawEqualLatTriangle (turtle, side):
# Question 2
    for _ in range(3):
        turtle.forward(side)
        turtle.left(120)

def turtleLeft (turtle, x, y):
# Question 6 changed turtle left realignment into function
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    
def main():
    # named constants
    screen_size = 500
    screen_startx = 60 # x coordinate of the left edge of the graphics window

    # Set up the window and its attributes
    wn = turtle.Screen()              
    wn.bgcolor("yellow")
    wn.setup(screen_size, screen_size, screen_startx, 0)

    axel = turtle.Turtle()
    axel.speed(7)

    # Initial turtle position near left edge, toward the bottom
    xpos = -screen_size/2 + 20 
    ypos = -screen_size/2 + 50   
    axel.up()
    axel.goto(xpos,ypos)
    axel.down()
    
    # y-dimension of each rectangle
    width = 50
    
    # draw three sets of shapes - same width(y-dimension) but different lengths
    for length in [25, 55, 75]:
 
        tri_side = getSide(length,width) 
        # Question 3
        
        radius = getRad(length,width)
        # Question 4
        
        # Draw the rectangle
        drawRect(axel, length, width)       
        # Here's code to draw a rectangle - before putting in a function
        # for side in [length, width, length, width]:
            #axel.forward(side)
            #axel.left(90)

        # Draw an equilateral triangle with sides the same as rectangle length    
        drawEqualLatTriangle (axel, length)
        # Question 2 call 1
        
        # Move a little to the right of the rectangle
        axel.up()
        axel.forward(2*length)
        axel.down()

        # Draw a circle with the same area as the rectangle      
        drawFillCircle (axel, radius)
        # Question 1 call 1
        
        # Move a little to the right of the circle
        axel.up()
        axel.forward(2*radius)
        axel.down()
        
        # Draw an equilateral triangle with same area as rectangle      
        drawEqualLatTriangle (axel, tri_side)
        # Question 2 call 2

        # Move a little to the right of the triangle
        axel.up()
        axel.forward(2*tri_side)
        axel.down()
        
        
        # Draw a circle with the same diameter as the triangle side
        drawFillCircle (axel, (tri_side/2))
        # Question 1 call 2
        
        # Calculate the next vertical position for a set of shapes
        ypos = next_y_position(ypos, tri_side)
        
        # Put turtle to left side of screen at correct height
        # Question 6 changed turtle left realignment into function call
        turtleLeft (axel, xpos, ypos)
        
        
       
    # Close window nicely after loop finishes
    wn.exitonclick()        

# Run the main function. This should be the last statement in the file.
main()


