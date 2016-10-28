"""PE4B"""


def fibo_sum_every_second(number):
    if number < 1:
        return 0
    now = 1
    previous = 0
    sum = 1
    for x in range(0, number - 1):
        if x % 2 == 0:
            now = now + previous
            previous = now - previous
            sum = sum + now
    return sum
print(fibo_sum_every_second(4))