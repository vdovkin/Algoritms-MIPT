def fibon(n):
    if n == 1 or n == 2:
        return 1

    return fibon(n - 1) + fibon(n - 2)


print(fibon(7))
