import turtle
import math

turtle.shape("turtle")


def draw_pental(radius, n=50):
    step = 2 * math.pi * radius / n
    engle = 360 / n

    n_one = n_two = n

    while n_one > 0:
        turtle.left(engle)
        turtle.forward(step)
        n_one -= 1

    while n_two > 0:
        turtle.right(engle)
        turtle.forward(step)
        n_two -= 1


N = 10
radius = 30
a = 10
turtle.left(90)

while N > 0:
    draw_pental(radius)
    radius += a
    N -= 1
