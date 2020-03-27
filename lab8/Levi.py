import turtle
import math


def levi(n, l):
    if n == 0:
        turtle.forward(l)
        return

    step = l / math.sqrt(2)

    turtle.left(45)
    levi(n - 1, step)

    turtle.right(90)
    levi(n - 1, step)

    turtle.left(45)


turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()
turtle.speed("fastest")

levi(6, 400)
