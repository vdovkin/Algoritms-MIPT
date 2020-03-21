import graphics as gr
import math

SIZE_X = 800
SIZE_Y = 800

window = gr.GraphWin("Model", SIZE_X, SIZE_Y)


def start_window():
    rectangle = gr.Rectangle(gr.Point(0, 0), gr.Point(SIZE_X, SIZE_Y))
    rectangle.setFill("green")
    rectangle.draw(window)

    center = gr.Circle(gr.Point(400, 300), 2)
    center.setFill("yellow")
    center.draw(window)


def pendulum(A, w, t):
    x = A * math.sin(w * t)
    return x


def get_new_coodrs(coords, old_x, new_x, center):
    new_x = coords.x + (new_x - old_x)
    new_y = (
        math.sqrt(
            (coords.x - center.x) ** 2
            - ((new_x - center.x) ** 2)
            + (coords.y - center.y) ** 2
        )
        + center.y
    )

    return gr.Point(new_x, new_y)


start_window()


coords_old = gr.Point(400, 700)
w = math.sqrt(9.81 / 400)
A = 200

circle = gr.Circle(coords_old, 10)
circle.setFill("red")

circle.draw(window)

line = gr.Line(gr.Point(400, 300), gr.Point(400, 700))
line.draw(window)

t = 0
old_x = 0

while True:
    new_x = pendulum(A, w, t)

    coords_new = get_new_coodrs(coords_old, old_x, new_x, gr.Point(400, 300))

    circle.move(coords_new.x - coords_old.x, coords_new.y - coords_old.y)

    line.undraw()
    window.update()
    line = gr.Line(gr.Point(400, 300), gr.Point(coords_new.x, coords_new.y))
    line.draw(window)

    coords_old = coords_new
    old_x = new_x

    t += 1
    gr.time.sleep(0.1)
