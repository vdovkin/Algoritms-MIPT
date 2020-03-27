# import sys


def fac_rec(n, deep=None):
    deep = deep or 0
    if n == 0:
        print(deep)
        return 1
    else:
        deep += 1
        return n * fac_rec(n - 1, deep=deep)


def fac_dec(n):
    f = 1
    x = 2
    while x <= n:
        f *= x
        x += 1

    return f


print(fac_rec(5))
print()
# print(fac_dec(5))
# print(sys.getrecursionlimit())
