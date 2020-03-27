def find(number, A):
    """ botn x в А и возвращает True, если такой есть
    False, если такого нет"""
    flag = False
    for x in A:
        if number == x:
            flag = True
    return flag


def generate_permutation(N: int, M: int = -1, prefix=None):
    """Генерирует перестановок N чисел в M позициях с префиксом prefix"""
    M = N if M == -1 else M  # по умолчанию N чисел в N позициях
    prefix = prefix or []

    if M == 0:
        print(*prefix)
        return

    for number in range(1, N + 1):
        if find(number, prefix):
            continue
        prefix.append(number)
        generate_permutation(N, M - 1, prefix)
        prefix.pop()


generate_permutation(3)
