import turtle

def drawPicture(theTurtle):
    ''' Draw a simple picture using a turtle '''
    theTurtle.forward(100)
    theTurtle.left(90)
    theTurtle.forward(100)
    theTurtle.left(90)
    theTurtle.forward(100)
    theTurtle.left(90)
    theTurtle.forward(100)
    theTurtle.left(90)

myTurtle = turtle.Turtle()  # Creates a new Turtle object
drawPicture(myTurtle)

turtle1 = turtle.Turtle()
turtle2 = turtle.Turtle()
turtle1.setpos(-50, -50)
turtle2.setpos(200, 100)
turtle1.forward(100)
turtle2.left(90)
turtle2.forward(100)
