import turtle


def minkovski(n, l):

    if n == 0:
        turtle.forward(l)
        return

    step = l / 4
    minkovski(n - 1, step)
    turtle.left(90)
    minkovski(n - 1, step)
    turtle.right(90)
    minkovski(n - 1, step)
    turtle.right(90)
    minkovski(n - 1, step)
    minkovski(n - 1, step)
    turtle.left(90)
    minkovski(n - 1, step)
    turtle.left(90)
    minkovski(n - 1, step)
    turtle.right(90)
    minkovski(n - 1, step)


turtle.penup()
turtle.goto(-400, 0)
turtle.pendown()
turtle.speed("fastest")

minkovski(3, 800)
