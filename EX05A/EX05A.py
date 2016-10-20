"""Acronym making."""


def not_allowed_characters_check(text, chars):
    """Check not allowed characters.

    :param text: Input text.
    :param chars: Alphabet in use. (est/eng).
    :return: Return result of check.
    """
    text = text.lower()
    for i in text:
        if i not in chars and i != " ":
            return True
    return False


def len_of_list(text):
    """Count words in input text.

    :param text: Input text.
    :return: Return number of words in input text.
    """
    return len(text.split())


def acronym(text, chars, nr_of_words_limit):
    """Create acronym of input text.

    :param text: Input text.
    :param chars: Alphabet in use. (est/eng).
    :param nr_of_words_limit: Limit of words in input text.
    :return: Return acronym of input text.
    """
    if not_allowed_characters_check(text, chars):
        return "Input: " + "\"" + text +\
               "\"" + " contains not allowed characters!"
    if len_of_list(text) > nr_of_words_limit:
        return "Input: " + "\"" + text + "\"" +\
               " is too long (max length is " +\
               str(nr_of_words_limit) + " words)!"
    text = text.split()
    letters = ""
    for every_word in text:
        letters += every_word[0]
    letters = letters.upper()
    return letters


def main():
    """Print acronym."""
    nr_of_words_limit = 2
    chars = "abcdefghijklmnopqrstuvwõäöüxyz"
    print(acronym("National Geographics", chars, nr_of_words_limit))
main()
