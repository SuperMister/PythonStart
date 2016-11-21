"""Tests."""


import EX11A

object_list = EX11A.Disarrange()


def test_add_value_adding():
    """Test."""
    assert len(object_list.add_value(5)) == 1


def test_add_value_not_none():
    """Test."""
    assert object_list.add_value is not None


def test_add_value_type():
    """Test."""
    assert isinstance(object_list.add_value(5), list)


def test_new_order_changing():
    """Test."""
    object_list.add_value(2)
    object_list.add_value(5)
    object_list.add_value(9)
    assert object_list.new_order() != [2, 5, 9]


def test_new_order_type():
    """Test."""
    assert isinstance(object_list.add_value(5), list)


def test_new_order_not_none():
    """Test."""
    assert object_list.new_order() is not None


def test_get_list_initial():
    """Test."""
    object_list.initial_list = []
    object_list.initial_list = [2, 5, 9]
    assert object_list.get_list("initial") == [2, 5, 9]


def test_get_list_result():
    """Test."""
    assert object_list.get_list("result") != [2, 5, 9]


def test_get_list_length():
    """Test."""
    object_list.initial_list = []
    object_list.result_list = []
    object_list.initial_list = [2, 5, 9]
    object_list.new_order()
    assert len(object_list.get_list("result")) == len(object_list.get_list("initial"))
