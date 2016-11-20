"""Tests."""

import EX10B


def test_random_for_type():
    """Test."""
    assert isinstance(EX10B.random_string("abcdefg", 2), str)


def test_random_not_none():
    """Test."""
    assert EX10B.random_string("abcdefg", 2) is not None


def test_random_len():
    """Test."""
    assert len(EX10B.random_string("abcdefg", 2)) > 0


def test_check_not_none():
    """Test."""
    assert EX10B.check_string("abcdefg", "adc") is not None


def test_check_find():
    """Test."""
    assert EX10B.check_string("abcdefg", "abc") is True


def test_check_not_find():
    """Test."""
    assert EX10B.check_string("abcdefg", "adc") is False


def test_check_for_type():
    """Test."""
    assert isinstance(EX10B.check_string("abcdefg", "abc"), bool)


def test_monkeyday_for_type():
    """Test."""
    assert isinstance(EX10B.monkey_day("abcdefg"), bool)


def test_monkeyday_not_none():
    """Test."""
    assert EX10B.monkey_day("abcdefg") is not None


