"""Fibonacci calcul."""


def fibonacci_sum(n):
    """
    :param n: Last fibonacci number.
    :return: "Return summary of all numbers before and including n"
    """

    if n == 0:
        return 0
    now = 1
    previous = 0
    sum = 1
    for x in range(0, n - 1):
        now = now + previous
        previous = now - previous
        sum = sum + now
    return sum
print(fibonacci_sum(1))
