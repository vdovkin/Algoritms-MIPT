#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_6():
    n_fill = 0
    while n_fill != 5:
        move_right()
        if cell_is_filled():
            n_fill += 1


if __name__ == "__main__":
    run_tasks()
