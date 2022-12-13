#Assignment 3, Turtle/for loop project
#Raymond Cheung
#09/13/2022
#This program prints 4 different colored decagons spaced evenly apart in square formation based on number of decagons drawn.

import turtle
wn= turtle.Screen()
decagon=turtle.Turtle()
side= 25 #set variable for decagon side length
angle= 36 #set angle needed for decagon shape (360/total number of sides) deca = 10 sides
for decagonColor in ["blue", "green", "yellow", "red"]: #outer loop that sets the amount of decagons (4) the turtles gonna draw, as well as the the color it will be
    for decagonDrawer in range(10): # not sure how much extra credit it's worth but inner loop that draws the decagons as wells as set the color based on outer loop list
        decagon.color(decagonColor)
        decagon.forward(side)
        decagon.right(angle)
    decagon.up ()#picks up pen so it doesnt drag the line through the 4 decagons
    decagon.left (90) # angles turtle to different spot
    decagon.forward (80) #moves the turtle to different location, so it doesnt overlap
    decagon.down () #sets pen down to start drawing new decagon
wn.exitonclick() 