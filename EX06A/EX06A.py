"""Control ID."""


def calculate_check_digit(personal_ID_nr_first_10_digits):
    """Generate ID control number.

    :param personal_ID_nr_first_10_digits: First 10 ID numbers.
    :return: Return control number.
    """
    control_number = 0
    personal_ID_nr_first_10_digits = str(personal_ID_nr_first_10_digits)
    for i in range(10):
        control_number += int(personal_ID_nr_first_10_digits[i]) * \
                          ((i % 9) + 1)

    control_number %= 11

    if control_number == 10:
        control_number = 0
        for i in range(10):
            control_number += int(personal_ID_nr_first_10_digits[i]) * \
                              (((i + 2) % 9) + 1)
        control_number %= 11
        if control_number == 10:
            control_number = 0

    return control_number


def len_of_personal_ID(personal_ID_nr):
    """Count ID length.

    :param personal_ID_nr: Given ID.
    :return: Return number of digits in ID.
    """
    personal_ID_nr = str(personal_ID_nr)
    return len(personal_ID_nr)


def personal_ID_characters_check(personal_ID_nr):
    """Check for unresolved characters.

    :param personal_ID_nr: Given ID.
    :return: Return True if ID does not contain unresolved characters.
     Return False if ID contains unresolved characters.
    """
    personal_ID_nr = str(personal_ID_nr)
    numbers = "0123456789"
    for i in personal_ID_nr:
        if i not in numbers:
            return False
    return True


def gender_feature_check(personal_ID_nr):
    """Check for correctness of 1 number.

    :param personal_ID_nr: Gived ID.
    :return: Return True if first number is correct.
     Return False if first number is not correct.
    """
    personal_ID_nr = str(personal_ID_nr)
    if int(personal_ID_nr[0]) in range(1, 7):
            return True
    return False


def month_number_check(month):
    """Check if month input is right.

    :param month: Month
    :return: Return True if month number is right.
     Return False if month number is wrong.
    """
    month = int(month)
    if month in range(1, 13):
        return True
    return False


def max_days_in_month(year, month):
    """Count maximum days in given month.

    :param year: Given year.
    :param month: Given month.
    :return: Return maximum days in given month.
    """
    year = int(year)
    month = int(month)
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    max_days = days_in_month[month - 1]

    if month == 2 and year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        max_days = 29

    return max_days


def personal_ID_nr_check(personal_ID_nr):
    """Control ID.

    :param personal_ID_nr: Given ID.
    :return: Return result of ID test.
    """
    personal_ID_nr = str(personal_ID_nr)
    year = int(personal_ID_nr[1:3])
    month = int(personal_ID_nr[3:5])
    day = int(personal_ID_nr[5:7])
    if len_of_personal_ID(personal_ID_nr) != 11:
        return 'Personal ID number is incorrect – wrong length'

    if not personal_ID_characters_check(personal_ID_nr):
        return 'Personal ID number is incorrect – contains incorrect symbols'

    if not gender_feature_check(personal_ID_nr):
        return 'Personal ID number is incorrect – wrong first number'

    if not month_number_check(month):
        return 'Personal ID number is incorrect – wrong month number'

    if max_days_in_month(year, month) < day or day == 0:
        return 'Personal ID number is incorrect – wrong day number'

    if int(calculate_check_digit(personal_ID_nr[0:10])) !=\
            int(personal_ID_nr[10]):
        return 'Personal ID number is incorrect – wrong check digit'

    return 'Personal ID number is correct!'
print(personal_ID_nr_check("39707250820"))
