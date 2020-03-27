import turtle


def cantor(n, l, x=-200, y=200):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.forward(l)

    if n == 0:
        return

    step = l / 3

    cantor(n - 1, step, x=x, y=y - 50)
    cantor(n - 1, step, x=x + 2 * step, y=y - 50)


# turtle.penup()
# turtle.goto(START_POINT)
# turtle.pendown()
# turtle.speed("fastest")

cantor(6, 400)
