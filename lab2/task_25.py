#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_2():
    move_right()
    move_down()
    for i in range(4):
        draw_plus()
        move_right(5)
        move_up()

    draw_plus()
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
