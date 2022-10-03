import turtle

# create the screen
wn = turtle.Screen()

# setup the canvas
wn.title("Turtle 1.O")
wn.setup(width=800, height=600)
turtle.bgcolor("black")
turtle.pencolor("white")

# setup the turtle
turtle.speed(0)
turtle.hideturtle()

# set the start position
turtle.penup()
turtle.goto(-2, 0)
turtle.pendown()

try:
    for i in range(1, 10920):
        turtle.circle(1 + i, 2 + i, 3 + i)
    turtle.update()
    turtle.done()
except turtle.Terminator:
    print('Program terminated')
    pass
