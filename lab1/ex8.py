import turtle


turtle.shape("turtle")

a = 10
N = 100
s_len = a

while N > 0:

    n = 2

    while n > 0:
        turtle.forward(s_len)
        turtle.left(90)
        n -= 1

    s_len += a
    N -= 1
