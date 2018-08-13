# Makes sure that 
import turtle


def drawM(theTurtle, xStart, yStart):
''' Draws letter M then moves turtle forward '''
    # Keeps track of initial position of the turtle
    curX = xStart
    curY = yStart

    displacementLists = [(0, 100), (50, 50), (100, 100), (100, 0)]

    # Used list of displacements from the original position, for sleeker/more readable code
    for coordinate in displacementLists:
        curX = xStart + coordinate[0]
        curY = yStart + coordinate[1]
        theTurtle.goto(curX, curY)


""" OLD VERSION OF PROGRAM
    Used repetitive code, replaced with for loop and list of displacements """
#    theTurtle.setheading(90)
#    theTurtle.forward(100)
#
#    curX = xStart + 50
#    curY = yStart + 50
#    theTurtle.goto(curX, curY)
#
#    curX = xStart + 100
#    curY = yStart + 100
#    theTurtle.goto(curX, curY)
#
#    curX = xStart + 100
#    curY = yStart
#    theTurtle.goto(curX, curY)

    # Gets turtle ready for more text input
    theTurtle.pu()
    curX = xStart + 110
    theTurtle.goto(curX, yStart)
    theTurtle.pd()

# Creates turtle object
myTurtle = turtle.Turtle()

# Calls function, and passes current coordinates
drawM(myTurtle, myTurtle.xcor(), myTurtle.ycor())
drawM(myTurtle, myTurtle.xcor(), myTurtle.ycor())
drawM(myTurtle, myTurtle.xcor(), myTurtle.ycor())
drawM(myTurtle, myTurtle.xcor(), myTurtle.ycor())

