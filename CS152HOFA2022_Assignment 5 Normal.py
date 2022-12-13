# Create several turtles and have them jump around randomly
# Record each position on the screen with a text description of the location
# 
# John Cigas, 9/25/2019
# Altered by Raymond Cheung 9/26/2022 
# Assignment 5
import turtle
import random

def myRand(sz):
    """ Returns a random integer in the range -sz to sz """
    return random.randrange(-sz, sz)

def getLocation (t):
    """ Returns a string with the location of turtle t """
    #used pluses instead of ","so the formatting on the screen looks cleaner
    return "I'm at "+  str(t.position ())+ '.' 

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
    for _ in range(3):
        # Move 1st turtle
        mrT.goto(myRand(width),myRand(height))
        mrT.stamp()
        loc = getLocation (mrT)
        mrT.write(loc)
        # Move 2nd turtle
        msPacMan.goto(myRand(width),myRand(height))
        msPacMan.stamp()
        loc = getLocation (msPacMan)
        msPacMan.write(loc)
        # Put your code here for msPacMan

        # Move 3rd turtle
        babyHuey.goto(myRand(width),myRand(height))
        babyHuey.stamp()
        loc = getLocation (babyHuey)
        babyHuey.write(loc)
        # Put your code here for babyHuey


# Start the program        
main()
