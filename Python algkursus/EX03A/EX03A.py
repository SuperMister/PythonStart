"""Fibonacci calcul."""


def fibonacci_sum(n):
    """
    :param n:
    :return:
    """
    now = 1
    previous = 1
    sum = 0
    for x in range(0, n+1):
        now = now + previous
        previous = now - previous
        sum = sum + now
    return sum
print(fibonacci_sum(5))