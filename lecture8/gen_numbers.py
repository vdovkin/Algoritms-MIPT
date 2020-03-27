def generate_numbers(N: int, M: int, prefix=None):
    prefix = prefix or []

    if M == 0:
        print(prefix)
        return

    for digit in range(N):
        prefix.append(digit)
        generate_numbers(N, M - 1, prefix)
        prefix.pop()


generate_numbers(2, 3)
