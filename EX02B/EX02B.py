"""
:param initial_amount: esmane investeeringu summa
:param amount: igakuine investeeringu summa
:param inv_percent: aastane intressi protsent
:param years: investeerimisaastate arv
Intressi arvestatakse igal kuul
:return: kui palju raha (investeeringusumma + intressitulu) on võimalik etteantud aastate pärast tagasi saada
"""
def investment(initial_amount, month_amount, inv_percent, years):
    for x in range (0, (years*12)):
        if(x == 0):
            initial_amount = initial_amount * ((1 + ((inv_percent/100)/12)))
        else:
            initial_amount = (initial_amount + month_amount)  * ((1 + ((inv_percent / 100) / 12)))
    return initial_amount
print(investment(1000, 0, 20, 1))