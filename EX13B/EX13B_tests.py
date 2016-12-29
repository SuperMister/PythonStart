"""EX13B tests."""

import EX13B

a = EX13B.FindPair("Test")
b = EX13B.FindPair("Test for small")
c = EX13B.FindPair("Blank")


def test_file_to_dict():
    """Test if function is converting file to dictionary."""
    assert c.file_to_dict() == "This file is empty, sorry!"
    assert isinstance(a.file_to_dict(), dict)
    assert isinstance(b.file_to_dict(), dict)
    assert sorted(list(a.dict_groups.keys())) == sorted(['t?druk', 'vana naine', 'poiss', 'mees', 'vana mees', 'naine'])


def test_biggest_group():
    """Test if function is finding biggest group."""
    assert isinstance(a.find_biggest_groups(), list)
    assert a.find_biggest_groups() == [['Peeter', 'Ants', 'Juhan', 'Rudolf']]


def test_find_pair():
    """Test if group are generating pairs that is not same."""
    for i in a.find_pair():
        for j in i:
            assert j.split("\t")[0] != j.split("\t")[1]
    assert isinstance(a.find_pair(), list)
    for i in a.big_groups:
        a.big_groups.count(i) == 1


def test_control_for_small():
    """Test if function is controlling file for small groups."""
    assert b.control_for_small_groups() == []
    assert a.control_for_small_groups() is not []


def test_output():
    """Test if function is giving output."""
    assert a.print_output() is None
