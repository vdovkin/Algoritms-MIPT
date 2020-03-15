import turtle
import math

turtle.shape("turtle")


def draw_arc(radius, n=50):
    step = 2 * math.pi * radius / n
    engle = 180 / n

    while n > 0:
        turtle.right(engle)
        turtle.forward(step)
        n -= 1


N = 10
radius_big = 40
radius_small = 10

turtle.left(90)

while N > 0:
    draw_arc(radius_big)
    draw_arc(radius_small)
    N -= 1
