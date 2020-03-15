#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_18():
    global ax
    ax = 0

    while not wall_is_on_the_right():
        if not wall_is_above():
            go_up()
            move_right()
        else:
            fill_cell()
            move_right()

        mov("ax", ax)


def go_up():
    global ax
    move_up()

    while not wall_is_above():
        if cell_is_filled():
            ax += 1
        else:
            fill_cell()
        move_up()

    if cell_is_filled():
        ax += 1
    else:
        fill_cell()

    while not wall_is_beneath():
        move_down()


if __name__ == "__main__":
    run_tasks()
