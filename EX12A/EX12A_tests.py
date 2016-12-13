"""Tests."""


import EX12A


def test_replace_html_replaces():
    """Test if function replaces html chars with umlauts."""
    assert EX12A.replace_html_encoding_with_umlauts("v&otilde;it") == "võit"


def test_replace_html_replaces_all_htmls():
    """Test if function replaces all html chars with umlauts."""
    assert EX12A.replace_html_encoding_with_umlauts("j&auml;&auml;tis") == "jäätis"


def test_if_no_html_chars_replace_nothing():
    """Test if function do not replace html chard if there is not umlauts chars. """
    assert EX12A.replace_html_encoding_with_umlauts("diivan") == "diivan"


def test_separate_base_form():
    """Test if function takes base form from the line."""
    assert EX12A.separate_base_form("uudise    uudis+0 //_S_ com sg gen //") == "uudis"


def test_separate_base_form_string():
    """Test if function return string."""
    assert isinstance(EX12A.separate_base_form("uudise    uudis+0 //_S_ com sg gen //"), str)


def test_read_from_file():
    """Test if function reads lines from file and converts them to the list. """
    assert EX12A.read_from_file("test.txt") == ['Kaks    kaks+0 //_N_ card sg nom l //']