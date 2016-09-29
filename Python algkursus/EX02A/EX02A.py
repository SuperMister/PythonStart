
"""Profit calcul."""


def profit(amount, days):
    """Count profit.

    :param amount: investeeritud summa
    :param days: päevade arv
    :intress: 1% (kapitaliseeritud intress)
    :return: intressist saadav tulu
    """
    income = amount
    for x in range(0, days):
        income *= 1.01
    return income - amount
print(profit(100, 9))
