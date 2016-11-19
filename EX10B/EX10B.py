"""EX10B."""


import random


def main():
    """Main function.

    :return: Return True if monkeys have written given word, otherwise return False.
    """
    pattern, simulations, num_of_monkeys = get_inputs()
    return monkey_day(pattern)


def random_string(chars, length):
    """Generate random word with given length and given characters.

    :param chars: Available characters.
    :param length: Length of the word.
    :return: Return random word from the available characters and with given length.
    """
    word = ""
    for i in range(length):
        word += random.choice(chars)
    return word


def check_string(text, pattern):
    """Control if word is in text.

    :param text: Text given.
    :param pattern: Given word.
    :return: Return True if word is in text, otherwise return False.
    """
    return pattern.lower() in text.lower()


def monkey_day(pattern):
    """Control if monkeys will find a given word within a day.

    :param pattern: Word that we want to control.
    :return: Return True if monkeys have written given word, otherwise return False.
    """
    num_of_monkeys = 10
    number_of_operations = 4 * 3600  # number_of_operations = seconds
    pattern = pattern.upper()
    all_monkeys = [""] * num_of_monkeys
    for x in range(number_of_operations):  # number_of_operations = seconds
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


def monkey_day_2(pattern, num_of_monkeys, number_of_operations=4 * 3600):
    """Control if monkeys will find a given word within a day.

    :param pattern: Given word.
    :param num_of_monkeys: Number of monkeys.
    :param number_of_operations: Number of operations to do.
    :return: Return True if monkeys have written given word, otherwise return False.
    """
    pattern = pattern.upper()
    all_monkeys = [""] * num_of_monkeys

    for x in range(number_of_operations):  # number_of_operations = seconds
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
    """Get inputs from user.

    :return: Return word, number of simulations and number of monkeys that user has entered.
    """
    word = input("Write your word: ")
    simulations = int(input("Number of simulations: "))
    monkeys = int(input("Number of monkeys: "))
    return word, simulations, monkeys

print(main())
