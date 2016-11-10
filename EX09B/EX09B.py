"""EUR."""


def euro_rates_main():
    """Print Euro maximum and minimum rate. Print how many times Euro was in the bottom and in the top half.

    :return: Return Euro maximum and minimum rate. Return how many times Euro was in the bottom and in the top half.
    """
    file = "1 EUR_X USD.txt"
    dates = []
    rates = []
    for i in read_from_file(file):
        dates.append(i.split("\t")[0])
        rates.append(float(i.split("\t")[1]))
    min = rates[seq_nr_of_min_rate(rates)]
    max = rates[seq_nr_of_max_rate(rates)]
    first = "Euro minimum rate: " + str(min) + " USD in " + str(dates[seq_nr_of_min_rate(rates)])
    second = "Euro maximum rate: " + str(max) + " USD in " + str(dates[seq_nr_of_max_rate(rates)])
    third = "Euro was " + str(number_of_rates_in_range(rates, min, (max + min) / 2)) + " times in the bottom half"
    fourth = "Euro was " + str(number_of_rates_in_range(rates, (min + max) / 2, max)) + " times in the top half"
    return first + "\n" + second + "\n" + third + "\n" + fourth


def read_from_file(file):
    """Convert file info to list.

    :param file: File that function reads from.
    :return: Return list of info that was in file.
    """
    list_of_dates_and_rates = []
    txt_file = open(file)
    for line in txt_file:
        if line.rstrip("\n") != "":
            list_of_dates_and_rates.append(line.rstrip("\n"))
    return list_of_dates_and_rates


def seq_nr_of_max_rate(rates):
    """Find the biggest rate of Euro.

    :param rates: List of EUR rates.
    :return: Return index of the biggest rate in list of EUR rates.
    """
    index_of_biggest_rate = 0
    current_index = 0
    current_biggest = 0
    for i in range(len(rates) - 1):
        current_index += 1
        if rates[i + 1] > rates[i]:
            current_biggest = current_index
            if rates[current_biggest] > rates[index_of_biggest_rate]:
                index_of_biggest_rate = current_biggest
    return index_of_biggest_rate


def seq_nr_of_min_rate(rates):
    """Find the lowest rate of EUR.

    :param rates: List of EUR rates.
    :return: Return index of the lowest rate in list of EUR rates.
    """
    index_of_smallest_rate = 0
    current_index = 0
    current_smallest = 0
    for i in range(len(rates) - 1):
        current_index += 1
        if rates[i + 1] < rates[i]:
            current_smallest = current_index
            if rates[current_smallest] < rates[index_of_smallest_rate]:
                index_of_smallest_rate = current_smallest
    return index_of_smallest_rate


def number_of_rates_in_range(rates, min, max):
    """Count how many times Euro rate was in the top half and in the bottom half.

    :param rates: List of EUR rates.
    :param min: Minimum limit for counting amount of rates.
    :param max: Maximum limit for counting amount of rates.
    :return: Return number of times when Euro was in the top half and in the bottom half.
    """
    number_of_rates = 0
    for i in rates:
        if min <= i <= max:
            number_of_rates += 1
    return number_of_rates
print(euro_rates_main())
