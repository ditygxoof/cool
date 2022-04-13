import turtle
t = turtle.Pen()
t.speed(0)
colors = ["red", "yellow", "blue", "green", "purple", "wheat", "tan", "plum"]

number_of_circles = int(turtle.numinput("Number of circles", "How many circles in your rosette?", 8))

for x in range(number_of_circles):
    t.pencolor(colors[x%8]) 
    t.circle(100)
    t.left(360/number_of_circles)
   
