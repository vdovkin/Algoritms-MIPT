#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    move_right()
    move_down()
    fill_cell()
    N = 12

    for i in range(12):
        for j in range(N):
            if not i % 2:
                move_right()
                move_down()
                fill_cell()
            else:
                move_left()
                move_up()
                fill_cell()

        if not i % 2:
            move_left()
            fill_cell()
        else:
            move_down()
            fill_cell()
        N -= 1

    move_down()


if __name__ == "__main__":
    run_tasks()
