def gcd(a, b):
    if a == b:
        return a
    elif a > b:
        return gcd(a - b, b)
    else:  # a < b
        return gcd(a, b - a)


def gcd_short(a, b):
    return a if b == 0 else gcd_short(b, a % b)
