import turtle
import math

turtle.shape("turtle")


def draw_star(n, radius=100):
    a = radius * 2 * math.sin(math.pi / n)

    h = math.sqrt(radius ** 2 - (a / 2) ** 2)
    H = h + radius
    alpha = 2 * math.atan(a / (2 * H)) * (180 / math.pi)
    l_move = math.sqrt(H ** 2 + (a / 2) ** 2)

    while n > 0:
        turtle.right(180 - alpha)
        turtle.forward(l_move)
        n -= 1


draw_star(5)
turtle.penup()
turtle.forward(300)
turtle.pendown()
draw_star(11)
