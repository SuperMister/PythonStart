"""Summarise every second element of fibonacci numbers."""

def fibo_sum_every_second(number):
    """Count summary of every second fibonacci number.

    :param number: Amount of fibonacci numbers given.
    :return: Return summary of every second fibonacci number.
    """
    if number < 1:
        return 0
    now = 1
    previous = 0
    sum = 0
    for x in range(0, number - 1):
        now += previous
        previous = now - previous
        if x % 2 == 0:
            sum += now
    return sum
print(fibo_sum_every_second(3))
