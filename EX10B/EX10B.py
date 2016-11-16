"""EX10B."""

import random

def main():
    chars = []
    for i in range(32, 256):
        chars += chr(i)
    return chars


def random_string(chars, length):
    word = ""
    for i in range(length + 1):
        word += random.choice(chars)
    return word


def check_string(text, pattern):
    if pattern in text:
        return True
    return False


def monkey_day(pattern):

