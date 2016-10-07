"""Caesar encode."""


def caesar_encode(text, shift):
    """Encode text with caesar method.

    :param text: Input text.
    :param shift: Number of changes in letter positions.
    :return: Return encoded text.
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    big_alphabet = alphabet.upper()

    encoded = ""
    for char in text:
        if char in alphabet:
            small_index = alphabet.index(char) + shift
            small_index %= len(alphabet)
            encoded += alphabet[small_index]
        elif char in big_alphabet:
            big_index = big_alphabet.index(char) + shift
            big_index %= len(big_alphabet)
            encoded += big_alphabet[big_index]
        else:
            encoded += char
    return encoded
print(caesar_encode("AAa!a", 1))
