"""Fibonacci summary."""


def fibonacci_sum(n):
    """
    :param n: last number in fibonacci
    :return: summary of last number and all numbers before
    """
    if n == 0:
        return 0
    now = 1
    previous = 0
    sum = 1
    for x in range (0, n-1):
        now = now + previous
        previous = now - previous
        sum = sum + now
    return sum
print(fibonacci_sum(0))
