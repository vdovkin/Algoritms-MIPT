#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    n_fill = 0
    n_empty = 0
    move_right()
    while not wall_is_on_the_right():
        if n_fill - n_empty > 1:
            move_right()
            n_empty += 1
        else:
            n_empty = 0
            fill_cell()
            move_right()
            n_fill += 1


if __name__ == "__main__":
    run_tasks()
