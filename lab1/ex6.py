import turtle

turtle.shape("turtle")

N = 12
Radius = 100

engle = 360 / N

while N > 0:
    turtle.forward(Radius)
    turtle.stamp()
    turtle.backward(Radius)
    turtle.left(engle)
    N -= 1
