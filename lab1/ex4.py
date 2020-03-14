import turtle
import math


turtle.shape("turtle")

N = 100
Radius = 100

step = 2 * math.pi * Radius / N
engle = 360 / N

while N > 0:
    turtle.forward(step)
    turtle.left(engle)
    N -= 1
