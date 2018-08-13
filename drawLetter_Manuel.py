import turtle

def drawM(theTurtle, xStart, yStart):
    curX = xStart
    curY = yStart
    theTurtle.setheading(90)
    theTurtle.forward(100)

    curX = xStart + 50
    curY = yStart + 50
    theTurtle.goto(curX, curY)

    curX = xStart + 100
    curY = yStart + 100
    theTurtle.goto(curX, curY)

    curX = xStart + 100
    curY = yStart
    theTurtle.goto(curX, curY)

    theTurtle.pu()
    curX = xStart + 110
    theTurtle.goto(curX, yStart)
    theTurtle.pd()

myTurtle = turtle.Turtle()

drawM(myTurtle, myTurtle.xcor(), myTurtle.ycor())
drawM(myTurtle, myTurtle.xcor(), myTurtle.ycor())
drawM(myTurtle, myTurtle.xcor(), myTurtle.ycor())
drawM(myTurtle, myTurtle.xcor(), myTurtle.ycor())

