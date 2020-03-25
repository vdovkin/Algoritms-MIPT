def matryoshka(n):
    if n == 1:
        print("Maтрёшечка")
    else:
        print("Вверх матрёшки n=", n)
        matryoshka(n - 1)
        print("Низ матрёшки n=", n)


matryoshka(5)
