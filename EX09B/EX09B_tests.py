"""Tests for EX09B."""


import EX09B


def test_empty_lines():
    """Test if function do not read empty lines."""
    assert EX09B.read_from_file("TEST for EMPTY LINES") == ['4.01.2016\t1.0898', '5.01.2016\t1.0746']


def test_wrong_answer():
    """Test if function converts txt.file to list."""
    assert EX09B.read_from_file("TEST for FIRST") == ['4.01.2016\t1.0898', '5.01.2016\t1.0746']


def test_type_of_output():
    """Test if function gives String as an output."""
    assert isinstance(EX09B.read_from_file("1 EUR_X USD.txt"), list)


def test_no_syntax_error():
    """Test if output is not SyntaxError."""
    assert EX09B.read_from_file("1 EUR_X USD.txt") != SyntaxError


def test_type_of_output_max():
    """Test if output is integer"""
    assert isinstance(EX09B.seq_nr_of_max_rate([0, 1, 3, 5, 7, 8]), int)


def test_index_of_biggest():
    """Test if function is outputting the minimum value."""
    assert EX09B.seq_nr_of_max_rate([0, 1, 4, 100, 5, 2]) == 3


def test_biggest_not_none():
    """Test if function output is not None."""
    assert EX09B.seq_nr_of_max_rate([0, 1, 4, 100, 5, 2]) is not None


def test_type_of_output_min():
    """Test if output is integer"""
    assert isinstance(EX09B.seq_nr_of_min_rate([0, 1, 3, 5, 7, 8]), int)


def test_index_of_smallest():
    """Test if function is outputting the minimum value."""
    assert EX09B.seq_nr_of_min_rate([0, 1, 4, 100, 5, 2]) == 0


def test_smallest_not_none():
    """Test if function output is not None."""
    assert EX09B.seq_nr_of_min_rate([0, 1, 4, 100, 5, 2]) is not None


def test_type_of_output_range():
    """Test if function output is integer."""
    assert isinstance(EX09B.number_of_rates_in_range([1, 3, 5 , 8, 11], 3 , 8), int)


def test_number_of_rates():
    """Test if function takes limits correctly."""
    assert EX09B.number_of_rates_in_range([1, 3, 5 , 8, 11], 3 , 8) == 3


def test_number_of_rates_for_syntax():
    """Test if output is not SyntaxError."""
    assert EX09B.number_of_rates_in_range([1, 3, 5 , 8, 11], 3 , 8) != SyntaxError


def test_euro_rates_main():
    """Test if function prints correctly."""
    assert EX09B.euro_rates_main() == "Euro minimum rate: 1.0742 USD in 6.01.2016" + "\n" + \
        "Euro maximum rate: 1.1569 USD in 3.05.2016" + "\n" + "Euro was 98 times in the bottom half" + "\n" + \
        "Euro was 116 times in the top half"


def test_euro_rates_main_type():
    """Test if function output is String."""
    assert isinstance(EX09B.euro_rates_main(), str)
