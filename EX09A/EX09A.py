"""EUR"""


def read_from_file(y):
    rows = []
    txt_file = open(y)
    for line in txt_file:
        if line.rstrip("\n") != "":
            rows.append(line.rstrip("\n"))
    return rows


def euro_rates_main():
    """

    :return:
    """
    y = "1 EUR_X USD.txt"
    dates = []
    rates = []
    for i in read_from_file(y):
        dates.append(i.split("\t")[0])
        rates.append(i.split("\t")[1])
    return "The longest increase of euro in USD is: " + str(the_longest_increase_of_euro(dates, rates))


def the_longest_increase_of_euro(dates, rates):
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
    longest_increase_dates = dates[biggest_start_of_period] + " (" + rates[biggest_start_of_period] + ") - " \
                             + dates[biggest_end_of_period] + " " + rates[biggest_end_of_period]
    return longest_increase_dates


print(euro_rates_main())
