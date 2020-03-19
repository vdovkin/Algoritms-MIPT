import graphics as gr

SIZE_X = 800
SIZE_Y = 800

window = gr.GraphWin("Model", SIZE_X, SIZE_Y)


def start_window():
    rectangle = gr.Rectangle(gr.Point(0, 0), gr.Point(SIZE_X, SIZE_Y))
    rectangle.setFill("green")
    rectangle.draw(window)

    center = gr.Circle(gr.Point(400, 200), 2)
    center.setFill("yellow")
    center.draw(window)


def add(point_1, point_2):
    new_point = gr.Point(point_1.x + point_2.x, point_1.y + point_2.y)

    return new_point


def sub(point_1, point_2):
    new_point = gr.Point(point_1.x - point_2.x, point_1.y - point_2.y)

    return new_point


def check_coords(coords, velocity):
    if coords.x < 0 or coords.x > SIZE_X:
        velocity.x = -velocity.x

    if coords.y < 0 or coords.y > SIZE_Y:
        velocity.y = -velocity.y


def update_coords(coords, velocity):
    return add(coords, velocity)


def update_velocity(velocity, acceleration):
    return add(velocity, acceleration)


def update_acceleration(ball_coords, center_coords):
    diff = sub(ball_coords, center_coords)
    distance_2 = (diff.x ** 2 + diff.y ** 2) ** (3 / 2)

    G = 2000

    return gr.Point(-diff.x * G / distance_2, -diff.y * G / distance_2)


start_window()


coords_old = gr.Point(400, 700)
velocity = gr.Point(2, 0)
acceleration = gr.Point(0, 0)

circle = gr.Circle(coords_old, 10)
circle.setFill("red")

circle.draw(window)

line = gr.Line(gr.Point(400, 200), gr.Point(400, 700))
line.draw(window)

while True:

    acceleration = update_acceleration(coords_old, gr.Point(400, 400))
    velocity = update_velocity(velocity, acceleration)
    coords_new = update_coords(coords_old, velocity)
    check_coords(coords_new, velocity)
    circle.move(coords_new.x - coords_old.x, coords_new.y - coords_old.y)
    line.undraw()
    window.update()
    line = gr.Line(gr.Point(400, 200), gr.Point(coords_new.x, coords_new.y))
    line.draw(window)

    coords_old = coords_new

    gr.time.sleep(0.02)
