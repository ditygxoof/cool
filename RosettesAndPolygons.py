import turtle
t = turtle.Pen()
colors = ["red", "yellow", "blue", "green", "purple", "wheat", "tan", "plum"]
sides = int(turtle.numinput("Number of sides", "How many sides in your spiral?", 4))
for m in range(5,75):
    t.left(360/sides + 5)
    t.width(m//25+1)
    t.penup()
    t.forward(m*4)
    t.pendown()
    if (m % 2 == 0):
        for n in range(sides):
            t.circle(m/3)
            t.right(360/sides)
            t.pencolor(colors[n%8]) 
    else:
        for n in range(sides):
            t.forward(m)
            t.right(360/sides)
            t.pencolor(colors[n%8]) 
