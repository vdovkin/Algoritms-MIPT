import turtle
import math


def dragon(n, l, sign=1):
    if n == 0:
        turtle.forward(l)
        return

    step = l / math.sqrt(2)

    turtle.left(45 * sign)
    dragon(n - 1, step, sign=1)

    turtle.right(90 * sign)
    dragon(n - 1, step, sign=-1)

    turtle.left(45 * sign)


turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()
turtle.speed("fastest")

dragon(10, 400)
