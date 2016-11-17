"""Tests."""


import EX10A


def test_if_sorted():
    """Test."""
    assert EX10A.is_sorted([1, 2, 3, 4, 5, 6, 7, 8, 9]) is True


def test_if_not_sorted():
    """Test."""
    assert EX10A.is_sorted([1, 2, 4, 5, 8, 1]) is False


def test_sorted_not_none():
    """Test."""
    assert EX10A.is_sorted([1, 2, 3, 4, 5, 7, 8, 9]) is not None


def test_if_list():
    """Test."""
    assert isinstance(EX10A.sort_random_elements([1, 2, 3, 4, 5, 6, 7, 8]), list)


def test_not_none():
    """Test."""
    assert EX10A.sort_random_elements([1, 2, 3, 4, 5, 6, 7, 8]) is not None


def test_if_changed():
    """Test."""
    assert EX10A.sort_random_elements([1, 2, 3, 4, 5, 6, 7, 8]) != SyntaxError


def test_number_of_operations():
    """Test."""
    assert EX10A.random_sort([8, 7, 6, 5, 4, 3, 2, 1])[1] > 0


def test_if_random_sort_list():
    """Test."""

    assert isinstance(EX10A.random_sort([1, 2, 3, 4, 5, 6, 7, 8])[0], list)


def test_if_random_sort_is_not_none():
    """Test."""
    assert EX10A.random_sort([1, 2, 3, 4, 5, 6, 7, 8]) is not None
