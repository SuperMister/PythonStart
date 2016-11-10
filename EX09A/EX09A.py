"""Count rise of EUR comparing to USD."""


def read_from_file(file):
    """Convert file info to list.

    :param file: File that function reads from.
    :return: Return list of info that was in file.
    """
    list = []
    txt_file = open(file)
    for line in txt_file:
        if line.rstrip("\n") != "":
            list.append(line.rstrip("\n"))
    return list


def euro_rates_main():
    """Give information about longest increase period of EUR.

    :return: String with info about longest increase period od EUR.
    """
    file = "1 EUR_X USD.txt"
    dates = []
    rates = []
    for i in read_from_file(file):
        dates.append(i.split("\t")[0])
        rates.append(i.split("\t")[1])
    return "The longest increase of euro in USD is: " + str(the_longest_increase_of_euro(dates, rates))


def the_longest_increase_of_euro(dates, rates):
    """Count the longest increase of EUR.

    :param dates: List of dates.
    :param rates: List of EUR rates.
    :return: Return String with the date of start of the longest period and EUR rate on this date
    and the date of the end of longest period and EUR rate on this date.
    """
    start = 0
    end = 0
    biggest_start_of_period = 0
    biggest_end_of_period = 0
    period_of_increase = 0
    for i in range(len(rates) - 1):
        if rates[i + 1] > rates[i]:
            end = i + 1
            if end > start:
                if end - start > period_of_increase:
                    period_of_increase = end - start
                    biggest_end_of_period = end
                    biggest_start_of_period = start
        elif rates[i + 1] < rates[i]:
            start = i + 1
    longest_increase_dates = dates[biggest_start_of_period] + " (" + str(rates[biggest_start_of_period]) + ") – " + \
        dates[biggest_end_of_period] + " " + "(" + str(rates[biggest_end_of_period]) + ")"
    return longest_increase_dates


print(euro_rates_main())
