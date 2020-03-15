#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.02)
def task_2_4():
    move_right()
    for i in range(5):
        if not i % 2:
            for j in range(9):
                draw_plus()
                move_right(5)
                move_up()
        else:
            for j in range(9):
                draw_plus()
                move_left(3)
                move_up()

        draw_plus()

        if i != 4:
            move_down(3)
            move_right()
        else:
            while not wall_is_on_the_left():
                move_left()

    move_up()


def draw_plus():
    fill_cell()

    move_right()
    move_down()
    fill_cell()

    move_down()
    move_left()
    fill_cell()

    move_up()
    fill_cell()

    move_left()
    fill_cell()


if __name__ == "__main__":
    run_tasks()
