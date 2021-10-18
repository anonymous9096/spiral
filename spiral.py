import turtle
from turtle import *

wn = turtle.Screen()
wn.title("Turtle 1.O")
wn.setup(width=800, height=600)
turtle.bgcolor("black")
turtle.pencolor("white")
turtle.hideturtle()

#objected, position

penup()
goto(-2, 0)
pendown()

# for i in range(1, 10920):
#     turtle.speed(0)
#     circle(5, 10, 2)
#     circle(5 + i, 10 + i, 2 + i)
#     i = i + 1
#     turtle.hideturtle()
#
# turtle.done()

for i in range(1, 10920):
    turtle.speed(0)
    circle(1, 2, 3)
    circle(1 + i, 2 + i, 3 + i)
    i = i + 1
    turtle.hideturtle()


turtle.update()
turtle.done()
