"""EX12A."""


import operator


def replace_html_encoding_with_umlauts(string):
    """Parast parandan."""
    return string.replace("&otilde;", "õ").replace("&ouml;", "ö").replace("&uuml;", "ü").replace("&auml;", "ä")


def separate_base_form(string):
    """Take the base form of the word."""
    string_list = list(string)
    base = []
    before_base = []
    for i in range(len(string_list) - 1):
        if string_list[i] == "+":
            before_base = string_list[:i]
            for i in range(1, len(before_base)):
                if before_base[i] != " " and before_base[i - 1] == " ":
                    base = (before_base[i:])
    base_string = "".join(base)
    return base_string.replace("=", "").replace("_", "")


def read_from_file(file):
    """Convert file info to list.

    :param file: File that function reads from.
    :return: Return list of info that was in file.
    """
    lines = []
    txt_file = open(file, 'r')
    for line in txt_file:
        if line.rstrip("\n") != "":
            lines.append(line.rstrip("\n"))
    txt_file.close()
    return lines


def amount_of_pairs(list_of_lines):
    """Find pairs."""
    pairs = {}
    for i in range(len(list_of_lines) - 1):
        if "_A_" in list_of_lines[i]:
            if "_S_" in list_of_lines[i + 1]:
                if replace_html_encoding_with_umlauts(separate_base_form(list_of_lines[i])) + " " + \
                        replace_html_encoding_with_umlauts(separate_base_form(list_of_lines[i + 1])) in pairs.keys():
                    pairs[replace_html_encoding_with_umlauts(separate_base_form(list_of_lines[i])) + " " +
                          replace_html_encoding_with_umlauts(separate_base_form(list_of_lines[i + 1]))] += 1
                else:
                    pairs[replace_html_encoding_with_umlauts(separate_base_form(list_of_lines[i])) + " " +
                          replace_html_encoding_with_umlauts(separate_base_form(list_of_lines[i + 1]))] = 1
    return pairs


def print_pairs_in_order(pairs, amount):
    """FFFFF."""
    pairs_sorted = sorted(pairs.items(), key=operator.itemgetter(1), reverse=True)
    if amount > len(pairs_sorted):
        print("There is not so many words.")
    else:
        for i in range(amount):
            print(pairs_sorted[i][0] + " " + str(pairs_sorted[i][1]))
