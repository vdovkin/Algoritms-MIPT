#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_30():
    width = 1
    while not wall_is_on_the_left():
        width += 1
        move_left()

    last_line, n_holle = line_test()
    move_left(width - 1)

    while not last_line:
        while not wall_is_beneath():
            move_down()

        last_line, n_holle = line_test()

        if not last_line:
            move_left(width - n_holle)
            move_down()
            while not wall_is_on_the_left():
                move_left()
    else:
        move_left(width - 1)


def line_test():
    i = 0
    j = 0
    last_line = True
    while not wall_is_on_the_right():
        i += 1
        if last_line and not wall_is_beneath():
            last_line = False
            j = i
        move_right()

    return (last_line, j)


if __name__ == "__main__":
    run_tasks()
