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
