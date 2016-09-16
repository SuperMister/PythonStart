"""
gffgdgdgdgdggfdgdgdfgg
"""

def profit(amount, days):
    income = amount
    for x in range(0, days):
        income = income * 1.01
    return income - amount
print(profit(100, 10))
