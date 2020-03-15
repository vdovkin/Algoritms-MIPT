import turtle
import math

turtle.shape("turtle")


def draw_polygon(radius, n):
    engle = 360 / n
    a = radius * 2 * math.sin(math.pi / n)

    turtle.left((180 - engle) / 2)

    while n > 0:
        turtle.left(engle)
        turtle.forward(a)
        n -= 1

    turtle.right((180 - engle) / 2)


N = 7
a = 20
n = 3
radius = a

while N > 0:

    draw_polygon(radius, n)

    turtle.penup()
    turtle.forward(a)
    turtle.pendown()

    radius += a
    n += 1
    N -= 1
