#Turtle will draw the letter D
import turtle
def drawD(theTurtle):
    theTurtle.left(90)
    theTurtle.forward(100)
    theTurtle.right(90)
    theTurtle.circle(-50,180)


myTurtle = turtle.Turtle()  
drawD(myTurtle)   
