"""EX13B tests."""

import EX13B

a = EX13B.FindPair("grupid.txt")


def test_file_to_dict():
    """Tests."""
    assert isinstance(a.file_to_dict(), dict)
    assert sorted(list(a.dict_groups.keys())) == sorted(['tпїЅdruk', 'vana naine', 'poiss', 'mees', 'vana mees', 'naine'])


def test_biggest_group():
    """Tests."""
    assert isinstance(a.find_biggest_group(), list)
    assert a.find_biggest_group() == ['Peeter', 'Ants', 'Juhan', 'Rudolf']


def test_find_pair():
    """Tests."""
    for i in a.find_pair():
        assert i.split("\t")[0] != i.split("\t")[1]
    assert isinstance(a.find_pair(), list)
    for i in a.all_pairs:
        a.all_pairs.count(i) == 1


def test_output():
    """Tests."""
    assert a.print_output() is None
