"""EX10B."""


import random


def main():
    """

    :return:
    """
    pattern, simulations, num_of_monkeys = get_inputs()
    return monkey_day(pattern, num_of_monkeys, simulations)


def random_string(chars, length):
    """

    :param chars:
    :param length:
    :return:
    """
    word = ""
    for i in range(length):
        word += random.choice(chars)
    return word


def check_string(text, pattern):
    """

    :param text:
    :param pattern:
    :return:
    """
    return pattern.lower() in text.lower()


def monkey_day(pattern, num_of_monkeys, number=4 * 3600):
    """

    :param pattern:
    :param num_of_monkeys:
    :param number:
    :return:
    """
    symbols = number
    pattern = pattern.upper()
    all_monkeys = [""] * num_of_monkeys
    for x in range(symbols):
        for i in range(len(all_monkeys)):
            random_sign = chr(random.randrange(65, 91))
            all_monkeys[i] += random_sign
            if all_monkeys[i][-1] == pattern[len(all_monkeys[i]) - 1]:
                if len(pattern) == len(all_monkeys[i]):
                    return True
            else:
                if all_monkeys[i][-1] == pattern[0]:
                    all_monkeys[i] = all_monkeys[i][-1]
                else:
                    all_monkeys[i] = str()
    return False


def get_inputs():
    """

    :return:
    """
    word = input("Write your word: ")
    simulations = int(input("Amount of simulations: "))
    monkeys = int(input("Amount of monkeys: "))
    return word, simulations, monkeys


print(main())
