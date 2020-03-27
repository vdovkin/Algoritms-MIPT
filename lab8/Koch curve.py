import turtle


def draw_curve(n, l):
    if n == 0:
        return

    if n == 1:
        turtle.forward(l / 3)
        turtle.left(60)
        turtle.forward(l / 3)
        turtle.right(120)
        turtle.forward(l / 3)
        turtle.left(60)
        turtle.forward(l / 3)

    draw_curve(n - 1, l / 3)
    turtle.left(60)
    draw_curve(n - 1, l / 3)
    turtle.right(120)
    draw_curve(n - 1, l / 3)
    turtle.left(60)
    draw_curve(n - 1, l / 3)


turtle.penup()
turtle.goto(-400, 0)
turtle.pendown()
turtle.speed("fastest")
draw_curve(5, 700)
