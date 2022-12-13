# Create several turtles and have them jump around randomly
# Record each position on the screen with a text description of the location
# 
# John Cigas, 9/25/2019
# Altered by Raymond Cheung 9/26/2022 
# Assignment 5 Extra Credit Version
import turtle
import random

def myRand(sz):
    """ Returns a random integer in the range -sz to sz """
    return random.randrange(-sz, sz)

def getLocation (t):
    """ Returns a string with the location of turtle t """
    #used pluses instead of ","so the formatting on the screen looks cleaner
    return "I'm at "+  str(t.position ())+ '.' 

def turtleTracker (turtle, width, height):
    #altered so that the three location per turtle are performed like original
    for repeatThree in range (3): 
        turtle.goto(myRand(width),myRand(height))
        turtle.stamp()
        loc = getLocation (turtle)
        turtle.write(loc)

def main():
    # define turtles
    wn = turtle.Screen()
    mrT = turtle.Turtle()
    msPacMan = turtle.Turtle()
    msPacMan.color("blue")
    babyHuey = turtle.Turtle()
    babyHuey.color("orange")

    # define screen bounds
    width = 225
    height = 250
    

    # draw turtles and their locations
    #EXTRA CREDIT change the turtle reporting location to a function and calling the function as a list with specified turtle name
    for listOfTurtles in [mrT, msPacMan, babyHuey]: 
        turtleTracker (listOfTurtles, width, height)
        


# Start the program        
main()
