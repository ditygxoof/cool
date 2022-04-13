import turtle
t = turtle.Pen()
t.speed(0)
t.turtlesize(2,2,2)
turtle.position()
(50,9)
def up():
    t.forward(50)
def left():
    t.left(90)
def right():
    t.right(90)
def down():
    t.penDown(90)
turtle.onkeypress(up, "Up")
turtle.onkeypress(left, "Left")
turtle.onkeypress(right, "Right")
turtle.onkeypress(down, "Down")
turtle.listen()
  
