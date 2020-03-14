import turtle

turtle.shape("turtle")

N = 10
step = 20
i = 0

while N > 0:
    i += 1
    n = 4

    while n > 0:
        turtle.forward(step)
        turtle.left(90)
        n -= 1

    turtle.penup()
    turtle.goto(-5 * i, -5 * i)
    turtle.pendown()

    step += 10
    N -= 1
