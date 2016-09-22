"""Fibonacci calcul."""


def fibonacci_sum(n):
    """
    Please describe here the content of this function, parameters and returnable value.
    :param n:
    :return:
    """


    now = 1
    previous = 0
    sum = 1
    for x in range (0, n-1):
        now = now + previous
        previous = now - previous
        sum = sum + now
    return sum
print(fibonacci_sum(5))
