
"""EUR."""


def euro_rates_main():
    """

    :return:
    """
    file = "1 EUR_X USD.txt"
    dates = []
    rates = []
    for i in read_from_file(file):
        dates.append(i.split("\t")[0])
        rates.append(i.split("\t")[1])
    min = rates[seq_nr_of_min_rate(rates)]
    max = rates[seq_nr_of_max_rate(rates)]
    first = "Euro minimum rate: " + str(min) + " USD in " + str(dates[seq_nr_of_min_rate(rates)])
    second = "Euro maximum rate: " + str(max) + " USD in " + str(dates[seq_nr_of_max_rate(rates)])
    third = "Euro was " + str(number_of_rates_in_range(rates, min, max)[0]) + " times in the bottom half"
    fourth = "Euro was " + str(number_of_rates_in_range(rates, min, max)[1]) + " times in the top half"
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
    """

    :param rates:
    :return:
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
    """

    :param rates:
    :return:
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
    """

    :param rates:
    :param min:
    :param max:
    :return:
    """
    middle_rate = (float(min) + float(max)) / 2
    min_interval = 0
    max_interval = 0
    for i in range(len(rates)):
        if float(rates[i]) < middle_rate:
            min_interval += 1
        elif float(rates[i]) > middle_rate:
            max_interval += 1
    return min_interval, max_interval

print(euro_rates_main())
