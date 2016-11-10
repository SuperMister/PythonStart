"""Tests for EX09A."""


import EX09A


def test_not_none():
    """Test if function output is not None."""
    assert EX09A.read_from_file("1 EUR_X USD.txt") is not None


def test_type_of_output():
    """Test if function gives String as an output."""
    assert isinstance(EX09A.read_from_file("1 EUR_X USD.txt"), list)


def test_no_syntax_error():
    """Test if output is not SyntaxError."""
    assert EX09A.read_from_file("1 EUR_X USD.txt") != SyntaxError


def test_type_of_output_of_increase():
    """Test if function gives String as an output."""
    assert isinstance(EX09A.the_longest_increase_of_euro(["4.01.2016"], ["1.0898"]), str)


def test_the_longest_increase_not_none():
    """Test if function do not return NONE."""
    assert EX09A.the_longest_increase_of_euro(["4.01.2016"], ["1.0898"]) is not None


def test_the_longest_increase_is_not_syntax():
    """Test if function output is not SyntaxError."""
    assert EX09A.the_longest_increase_of_euro(["4.01.2016"], ["1.0898"]) != SyntaxError


def test_type_of_output_of_main():
    """Test if function gives String as an output."""
    assert isinstance(EX09A.euro_rates_main(), str)


def test_output():
    """Test if function output is right."""
    assert EX09A.euro_rates_main() == "The longest increase of euro in USD is: 22.04.2016 (1.1263) – 3.05.2016 (1.1569)"
