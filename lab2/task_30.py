#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_9_3():
    size = 0
    while not wall_is_beneath():
        move_down()
        size += 1

    draw_squere(size)


def draw_squere(n):
    a = n // 2
    for i in range(a):
        move_right()
        for j in range(n - 1):
            fill_cell()
            move_right()
        move_up()
        for j in range(n - 1):
            fill_cell()
            move_up()
        move_left()
        for j in range(n - 1):
            fill_cell()
            move_left()
        move_down()
        for j in range(n - 1):
            fill_cell()
            move_down()

        move_right()
        move_up()
        n -= 2

    move_down(a)
    move_left(a)


if __name__ == "__main__":
    run_tasks()
