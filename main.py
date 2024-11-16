from profilehooks import profile


def fibonacci_rec(n: int) -> int:
    """Возвращает N-е число Фибоначчи. Реализована рекурсивно согласно
    формуле вычисления последовательности.

    :param n: порядковый номер числа Фибоначчи
    :return: число Фибоначчи
    """
    if n<= 0:
        return None
    if n == 1 or n ==2:
        return 1
    return fibonacci_rec(n-1)+fibonacci_rec(n-2)


def fibonacci_iter(n: int) -> int:
    """Возвращает N-е число Фибоначчи. Реализована итеративно с использованием
    массива для хранения вычисляемых данных.

    :param n: порядковый номер числа Фибоначчи
    :return: число Фибоначчи
    """
    if n<= 0:
        return None
    if n == 1 or n ==2:
        return 1
    arr = [0]*(n+1)
    arr[1] = arr[2] = 1
    for i in range (3, n+1):
        arr[i] = arr[i-1]+arr[i-2]
    return arr[n]



def fibonacci(n: int) -> int:
    """Возвращает N-е число Фибоначчи. Реализована итеративно без использования массива.

    :param n: порядковый номер числа Фибоначчи
    :return: число Фибоначчи
    """
    if n<= 0:
        return None
    if n == 1 or n ==2:
        return 1
    pred = 1
    predpred = 1
    for i in range (3, n+1):
        current = pred + predpred
        predpred = pred
        pred = current
    return pred


def main():
    n = 35
    print(f"Вычисление {n} числа Фибоначчи рекурсивно:")
    print(fibonacci_rec(n))

    print(f"\nВычисление {n} числа Фибоначчи итеративно:")
    print(fibonacci_iter(n))

    print(f"\nВычисление {n} числа Фибоначчи итеративно без использования массива:")
    print(fibonacci_iter(n))


if __name__ == "__main__":
    main()
