import turtle
import math

turtle.shape("turtle")

N = 500
a = 10
engle_step = 5 * math.pi / 180
engle = 0

while N > 0:
    engle_rad_1 = engle
    engle += engle_step
    engle_rad_2 = engle

    radius1 = a * engle_rad_1 / (2 * math.pi)
    radius2 = a * engle_rad_2 / (2 * math.pi)

    len_move = math.sqrt(
        (radius2 - radius1) ** 2 + (radius1 * math.sin(engle_step)) ** 2
    )

    turtle.forward(len_move)
    turtle.left(engle_step * 180 / math.pi)

    N -= 1
