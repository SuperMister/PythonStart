"""Tests for EX13A."""


import EX13A


test = EX13A.FindBusTime("bussiajad.txt")


def test_get_message():
    """Test if function is giving message."""
    assert test.get_message() == "Write your current time! "


def test_file_to_dict():
    """Test if function is outputting dictionary with right keys."""
    assert isinstance(test.dict_of_times, dict)
    assert list(test.file_to_dict().keys()) == [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]


def test_find_time():
    """Test if function if finding the most nearest buss departure for the given time."""
    assert test.find_time("12:30") == "Your buss will departure at 12:33"
    assert test.find_time("1:00") == "Your buss will departure at 5:26"
    assert test.find_time("23:58") == "Your buss will departure at 5:26"
