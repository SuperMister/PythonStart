import EX09A


def test_empty_lines():
    """Test if function do not read empty lines."""
    assert EX09A.read_from_file("TEST for EMPTY LINES") == ['4.01.2016\t1.0898', '5.01.2016\t1.0746']


def test_wrong_answer():
    """Test if function converts txt.file to list."""
    assert EX09A.read_from_file("TEST for FIRST") == ['4.01.2016\t1.0898', '5.01.2016\t1.0746']


def test_type_of_output():
    """Test if function gives String as an output."""
    assert isinstance(EX09A.read_from_file("1 EUR_X USD.txt"), list)


def test_type_of_output_of_increase():
    """Test if function gives String as an output."""
    assert isinstance(EX09A.the_longest_increase_of_euro(["4.01.2016"], ["1.0898"]), str)


def test_the_longest_increase_not_none():
    """Test if function do not return NONE."""
    assert EX09A.the_longest_increase_of_euro(["4.01.2016"], ["1.0898"]) is not None


def test_for_length_of_output():
    """Test if function output has a minimum possible length."""
    assert len(EX09A.the_longest_increase_of_euro(["4.01.2016"], ["1.0898"])) >= 37


def test_type_of_output_of_main():
    """Test if function gives String as an output."""
    assert isinstance(EX09A.euro_rates_main(), str)


def test_output():
    """Test if function output is right."""
    assert EX09A.euro_rates_main() == "The longest increase of euro in USD is: 22.04.2016 (1.1263) – 3.05.2016 (1.1569)"


def test_main_output_length():
    """Test if function output has a minimum possible length."""
    assert len(EX09A.euro_rates_main()) >= 77
