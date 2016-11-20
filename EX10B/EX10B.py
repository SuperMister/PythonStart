"""EX10B."""


import random


class Monkey:
    """Monkey actions."""

    def __init__(self, pattern):
        """Constructor."""
        self.text = str()
        self.word = pattern.upper()

    def push_button(self):
        """Monkey push button."""
        self.text += chr(random.randrange(65, 91))

    def check_last_written_char(self):
        """Monkey control last character written."""
        if self.text[-1] == self.word[len(self.text) - 1]:
            if len(self.text) == len(self.word):
                return True
        else:
            if self.text[-1] == self.word[0]:
                self.text = self.text[-1]
            else:
                self.text = str()


def main(word, monkeys, simulations):
    """Count average amount of days that monkeys need for typing given word.

    :return: Return average time that monkeys need for typing given word.
    """
    amounts_of_time = [""] * simulations
    for i in range(simulations):
        amounts_of_time[i] = monkeys_find_word(word, monkeys)

    all_time = 0
    for i in amounts_of_time:
        all_time += i
    average_time = int(all_time / simulations)
    return average_time


def random_string(chars, length):
    """Generate random word with given length and given characters.

    :param chars: Available characters.
    :param length: Length of the given word.
    :return: Return random word from the available characters and with given length.
    """
    word = ""
    for i in range(length):
        word += random.choice(chars)
    return word


def check_string(text, pattern):
    """Control if word is in text.

    :param text: Given text.
    :param pattern: Given word.
    :return: Return True if word is in text, otherwise return False.
    """
    return pattern.lower() in text.lower()


def monkey_day(pattern):
    """Control if monkey has written needed word in one day.

    :param pattern: Given word.
    :return: Return True if monkey has written needed word.
    """
    monkey = Monkey(pattern)
    for i in range(3600 * 4):
        monkey.push_button()
        if monkey.check_last_written_char():
            return True
    return False


def monkeys_find_word(pattern, num_of_monkeys):
    """Count how many days will it take for monkeys to type .

    :param pattern: Given word.
    :param num_of_monkeys: Number of monkeys that type.
    :return:
    """
    all_monkeys = [Monkey(pattern) for i in range(num_of_monkeys)]
    seconds = 0
    while True:
        for i in range(len(all_monkeys)):
            seconds += 1
            all_monkeys[i].push_button()
            if all_monkeys[i].check_last_written_char():
                return int(seconds / 3600 * 4)


def get_inputs():
    """Get info from user.

    :return: Return word, number of monkeys and number of simulations that user prefers.
    """
    word = input("Write your word: ")
    simulations = int(input("Amount of simulations: "))
    monkeys = int(input("Amount of monkeys: "))
    return word, monkeys, simulations


def print_output():
    """Print output."""
    pattern, num_of_monkeys, simulations = get_inputs()
    return "On the average it took " + str(main(pattern, num_of_monkeys, simulations)) \
           + " days for " + str(num_of_monkeys) + " monkeys to type the word " + "\"" + pattern + "\"" + ". " \
           + "Number of simulations: " + str(simulations) + "."
