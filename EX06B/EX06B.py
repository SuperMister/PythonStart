def find_gender_number(year, gender):
    first = 0
    if int(year) in range(1800, 1900):
        if gender == "M":
            first += 1
        if gender == "F":
            first += 2
    if int(year) in range(1900, 2000):
        if gender == "M":
            first += 3
        if gender == "F":
            first += 4
    if int(year) in range(2000, 2100):
        if gender == "M":
            first += 5
        if gender == "F":
            first += 6
    if int(year) in range(2100, 2200):
        if gender == "M":
            first += 7
        if gender == "F":
            first += 8
        first = str(first)
    return first


def max_days_in_month(year, month):
    year = int(year)
    month = int(month)
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    max_days = days_in_month[month - 1]

    if month == 2 and year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        max_days = 29

    return max_days

def validate_date(year, month, day):
    year = str(year)
    month = str(month)
    day = str(day)
    number = "0123456789"
    for num_year in year:
        if num_year not in number:
            return False
    if int(year) not in range(1900, 2100):
        return "Incorrect year (allowed 1900-2099)"
    for num_month in month:
        if num_month not in month:
            return False
    if int(month) not in range(1, 13):
        return "Incorrect month (allowed 1-12)"
    for num_day in day:
        if num_day not in number:
            return False
    month = int(month)
    if int(day) not in range(1, int(max_days_in_month(year, month)) + 1):
        return "Incorrect day (allowed 1-" + str(max_days_in_month(year, month)) + ")"
    return True

def find_general_number(hospital_index, sequence_nr):
    hospital_number = [1, 11, 21, 221, 271, 371, 421, 471, 491, 521, 571, 601, 651]
    if hospital_index not in range(1, 14):
        return False
    hospital_staff = int(hospital_number[hospital_index - 1]) + (sequence_nr - 1)
    if hospital_staff >= int(hospital_number[hospital_index]):
        return "0"
    hospital_staff = str(hospital_staff)
    if len(hospital_staff) == 1:
        return "00" + hospital_staff
    if len(hospital_staff) == 2:
        return "0" + hospital_staff
    return hospital_staff


def calculate_check_digit(personal_ID_nr_first_10_digits):
    """Generate ID control number.

    :param personal_ID_nr_first_10_digits: First 10 ID numbers.
    :return: Return control number.
    """
    control_number = 0
    for i in range(10):
        control_number += int(personal_ID_nr_first_10_digits[i]) * ((i % 9) + 1)

    control_number %= 11

    if control_number == 10:
        control_number = 0
        for i in range(10):
            control_number += int(personal_ID_nr_first_10_digits[i]) * (((i + 2) % 9) + 1)
        control_number %= 11
        if control_number == 10:
            control_number = 0

    return control_number


def personal_ID_nr(gender, year, month, day, hospital_index, sequence_nr):
    if gender != "M" and gender != "F":
        return "Incorrect gender (allowed 'M' or 'F')"
    if find_general_number(hospital_index, sequence_nr) == False:
        return "Incorrect hospital index number (allowed 1-13)"
    if find_general_number(hospital_index, sequence_nr) == "0":
        return "Incorrect person's sequence number (too big)"
    if validate_date(year, month, day) != True:
        return validate_date(year, month, day)

    year2 = str(year)
    year2 = year2[2:4]
    month = str(month)
    day = str(day)
    if len(month) == 1:
        month = "0" + month
    if len(day) == 1:
        day = "0" + day
    personal_ID_nr_first_10_digits = str(find_gender_number(year, gender)) + year2 + month + day +\
         find_general_number(hospital_index, sequence_nr)
    ID = str(find_gender_number(year, gender)) + year2 + month + day +\
        (find_general_number(hospital_index, sequence_nr) + str(calculate_check_digit(personal_ID_nr_first_10_digits)))
    return ID
print(personal_ID_nr('s', 1800 , 10,  1 , 10, 55))


