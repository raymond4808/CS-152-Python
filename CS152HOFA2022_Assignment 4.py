#Raymond Cheung
#09/20/2022
#Assignment 4
#This program prints 4 different colored and sized decagons randomly spaced apart, with each starting end marked with a turtle

import turtle
import random #assignment 4 NEW
wn= turtle.Screen()
decagon=turtle.Turtle()

decagon.speed (0) #assignment 4 NEW | new turtle function to speed up animation times
decagon.shape("turtle")#assignment 4 NEW turtle function | set shape from arrow to turtle

side= random.randrange (15, 35) #Assignment 4 NEW |set INITIAL random variable for decagon side length
spotRandom = random.randrange (-150, 150) #Assignement 4 NEW | sets random angle movement and distance values proportionate to turtle screen
angle= 36 #set angle needed for decagon shape (360/total number of sides) deca = 10 sides


for decagonColor in ["blue", "green", "yellow", "red"]: #outter loop that sets the amount of decagons (4) the turtles gonna draw, as well as the the color it will be
    for decagonDrawer in range(10): 
        decagon.color(decagonColor)
        decagon.forward(side)
        decagon.right(angle)
        
    decagon.stamp () #assignment 4 NEW use of turtle stamp function to show the starting side of decagon created
    side= random.randrange (15, 35) #Assignement 4 NEW | sets random side length each time a NEW decagon is created 
    
    #code chunk below sets new decagon to a random different location on the screen with out dragging the pen across the screen
    decagon.up ()
    decagon.left (spotRandom) 
    decagon.forward (spotRandom) 
    decagon.down () 
           
wn.exitonclick() 