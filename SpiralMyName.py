import turtle
t = turtle.Pen()
turtle.bgcolor("black")
colors = ["red", "yellow", "blue", "green"]

your_name = turtle.textinput("Enter your name", "What is your name?")
sides = int(turtle.numinput("Number of sides", "How many sides do you want (1-8)?", 4, 1, 8))


for x in range(100):
    t.pencolor(colors[x%sides])
    t.penup()
    t.forward(x*3/sides+x)
    t.pendown()
    t.write(your_name, font = ("Arial", int( (x+4) / 4), "bold"))
    t.left(100/sides+1)
    t.width(x*sides/200)

                            
