"""Make this list good."""


import random


def main():
    """Read from file and return answer.

    :return: Return sorted list and number of operations.
    """
    list_of_numbers = []
    with open("numbers.txt") as txt_file:
        for i in txt_file:
            list_of_numbers.append(int(i))
    return random_sort(list_of_numbers)


def random_sort(list_of_numbers):
    """Sort list and count number of operations done.

    :param list_of_numbers: List of numbers.
    :return: Return sorted list and number of operations done.
    """
    number_of_operations = 0
    while not is_sorted(list_of_numbers):
        for i in range(len(list_of_numbers)):
            sort_random_elements(list_of_numbers)
            number_of_operations += 1
    return list_of_numbers, number_of_operations


def is_sorted(list_of_numbers):
    """Control if list is sorted.

    :param list_of_numbers: List of numbers.
    :return: Return True if list is sorted.
    """
    for i in range(len(list_of_numbers) - 1):
        if list_of_numbers[i] > list_of_numbers[i + 1]:
            return False
    return True


def sort_random_elements(list_of_numbers):
    """Change 2 numbers if second number is bigger than the first one.

    :param list_of_numbers: List of numbers.
    :return: Return list of numbers with 2 numbers changed.
    """
    a = random.randrange(0, len(list_of_numbers))
    b = random.randrange(0, len(list_of_numbers))
    if a < b:
        if list_of_numbers[a] > list_of_numbers[b]:
            list_of_numbers[b], list_of_numbers[a] = list_of_numbers[a], list_of_numbers[b]
    elif a > b:
        if list_of_numbers[a] < list_of_numbers[b]:
            list_of_numbers[b], list_of_numbers[a] = list_of_numbers[a], list_of_numbers[b]
    return list_of_numbers
