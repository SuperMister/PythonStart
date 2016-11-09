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

