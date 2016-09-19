"""EX02B."""


def investment(initial_amount, month_amount, inv_percent, years):
    """
    Count intress amount.
    :param initial_amount: esmane investeeringu summa
    :param amount: igakuine investeeringu summa
    :param inv_percent: aastane intressi protsent
    :param years: investeerimisaastate arv(inglise keeles)kõik
    :return: income
    """
    for x in range(0, (years*12)):
        if(x == 0):
            initial_amount = initial_amount * ((1 + ((inv_percent/100)/12)))
        else:
            initial_amount = (initial_amount + month_amount) * \
                             ((1 + ((inv_percent / 100) / 12)))
    return initial_amount
print(investment(1000, 20, 10, 5))
