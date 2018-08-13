#Turtle will draw the letter D
import turtle
def drawD(theTurtle, size):
''' Draws the letter D, depending on the size given '''
    theTurtle.left(90)
    theTurtle.forward(100 * size)
    theTurtle.right(90)
    theTurtle.circle(-50 * size,180)


myTurtle = turtle.Turtle()
drawD(myTurtle, 2)
