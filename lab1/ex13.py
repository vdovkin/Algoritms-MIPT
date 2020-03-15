import turtle
import math

turtle.shape("turtle")


def draw_circle(radius, n=50):
    step = 2 * math.pi * radius / n
    engle = 360 / n

    while n > 0:
        turtle.left(engle)
        turtle.forward(step)
        n -= 1


def draw_arc(radius, n=50):
    step = 2 * math.pi * radius / n
    engle = 180 / n

    while n > 0:
        turtle.right(engle)
        turtle.forward(step)
        n -= 1


turtle.penup()
turtle.forward(200)
turtle.left(90)
turtle.pendown()

turtle.begin_fill()
draw_circle(200)
turtle.color("yellow")
turtle.end_fill()

turtle.penup()
turtle.goto(-60, 100)
turtle.pendown()

turtle.begin_fill()
turtle.color("blue")
draw_circle(20)
turtle.end_fill()

turtle.penup()
turtle.goto(100, 100)
turtle.pendown()

turtle.begin_fill()
turtle.color("blue")
draw_circle(20)
turtle.end_fill()

turtle.penup()
turtle.goto(0, 50)
turtle.pendown()
turtle.color("black")
turtle.width(10)
turtle.left(180)
turtle.forward(100)


turtle.penup()
turtle.goto(100, -50)
turtle.pendown()

turtle.color("red")
draw_arc(50)
