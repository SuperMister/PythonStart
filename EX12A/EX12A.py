"""EX12A."""


def replace_html_encoding_with_umlauts(string):
    return string.replace("&otilde", "õ").replace("&ouml", "ö").replace("&uuml", "ü").replace("&auml", "ä")
print(replace_html_encoding_with_umlauts("taas&ouml_ise_seisvu=mis_j&auml;rgne"))


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

print(separate_base_form("taasiseseisvumisj&auml;rgse    taas_ise_seisvu=mis_j&auml;rgne+0 //_A_ pos sg gen //"))



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


def get_pairs(list_of_lines):
    """Find paairs."""
    pairs = {}
    for i in range(len(list_of_lines) - 1):
        if "_A_" in list_of_lines[i]:
            if "_S_" in list_of_lines[i + 1]:
                if pairs.keys() in pairs.keys:
                    pairs[replace_html_encoding_with_umlauts(separate_base_form(list_of_lines[i])) +
                    replace_html_encoding_with_umlauts(separate_base_form(list_of_lines[i + 1]))] = 1

    return
print(get_pairs(read_from_file("aja_pm150699.kym.txt")))

