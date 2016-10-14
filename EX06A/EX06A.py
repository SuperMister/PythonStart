"""Count ID."""

def len_of_personal_ID(personal_ID_nr):
    personal_ID_nr = str(personal_ID_nr)
    return len(personal_ID_nr)

def personal_ID_characters_check(personal_ID_nr):
    personal_ID_nr = str(personal_ID_nr)
    numbers = "0123456789"
    for char in personal_ID_nr:
        if char not in numbers:
            return False
    return True

def gender_feature_check(personal_ID_nr):
    personal_ID_nr = str(personal_ID_nr)
    if int(personal_ID_nr[0]) >= 1 and int(personal_ID_nr[1]) <= 6:
        return True
    return False


def month_number_check(month):
    month = int(month)
    if month >= 1 and month <= 12:
        return True
    return False

def max_days_in_month(year, month):
    month = int(month)
    year = int(year)

    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    max_days = days_in_month[month - 1]

    if month == 2 and year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        max_days = 29

    return max_days

def calculate_check_digit(personal_ID_nr_first_10_digits):
    control_number = 0
    for i in range(0, 10):
        control_number = int(personal_ID_nr_first_10_digits[i]) * ((i % 9) + 1)

    control_number %= 11

    if control_number == 10:
        control_number = 0
        for y in range (0, 10):
            control_number = int(personal_ID_nr_first_10_digits[y]) * (((y + 2) % 9) + 1)
        if control_number == 10:
            control_number = 0

    return control_number

def personal_ID_nr_check(personal_ID_nr):
    personal_ID_nr = str(personal_ID_nr)
    year = int(personal_ID_nr[1:3])
    month = int(personal_ID_nr[3:5])
    day = int(personal_ID_nr[5:7])

    if len_of_personal_ID(personal_ID_nr) != 11:
        return "Personal ID number is incorrect - wrong length"

    if not personal_ID_characters_check(personal_ID_nr):
        return "Personal ID number is incorrect - contains incorrect symbols"

    if gender_feature_check(personal_ID_nr):
        return "Personal ID number is incorrect - wrong first number"

    if not month_number_check(month):
        return "Personal ID number is incorrect - wrong month number"

    if max_days_in_month(year, month) < day or day == 0:
        return "Personal ID number is incorrect - wrong day number"

    if int(calculate_check_digit(personal_ID_nr[0:10])) != int(personal_ID_nr[10]):
        return "Personal ID number is incorrect - wrong check digit"

    return "Personal ID number is correct!"

print(personal_ID_nr_check("a9810015521"))
print(personal_ID_nr_check("89810015521"))
print(personal_ID_nr_check("49813015521"))
print(personal_ID_nr_check("49802315520"))
print(personal_ID_nr_check("49810015520"))
print(personal_ID_nr_check("498100155289"))
print(personal_ID_nr_check("4981001552"))
print(personal_ID_nr_check("49810015028"))
print(personal_ID_nr_check("39707250820"))
