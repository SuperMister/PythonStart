"""Tests."""


import EX12B

syn1 = EX12B.Synonym(['nimekiri', 'nimestik', 'loend'])
syn2 = EX12B.Synonym(['järjend', 'jada', 'sequence'])
syn_dict = EX12B.SynonymDictionary([syn1])


def test_add_synonym():
    """Test if function is adding synonym to the list of synonyms."""
    syn1.add("one more")
    syn2.add("or")
    syn2.add("two")
    assert syn1.list() == sorted(['nimekiri', 'nimestik', 'loend', "one more"])
    assert syn2.list() == sorted(['järjend', 'jada', 'sequence', "or", "two"])


def test_remove_synonym():
    """Test if function removes synonyms."""
    syn1.remove("one more")
    syn2.remove("two")
    assert syn1.list() == sorted(['nimekiri', 'nimestik', 'loend'])
    assert syn2.list() == sorted(['järjend', 'jada', 'sequence', "or"])


def test_if_list_sorted():
    """Test if function return sorted list of synonyms."""
    assert syn1.list() != ['nimekiri', 'nimestik', 'loend']
    assert syn2.list() != ['järjend', 'jada', 'sequence', "or"]


def test_find_in_dictionary():
    """Test if function is finding a synonyms for the given word."""
    assert syn_dict.find("loend") == sorted(['nimekiri', 'nimestik'])


def test_add_list_to_dictionary():
    """Test if function is adding a new list of synonyms to the dictionary."""
    syn_dict.add(syn2)
    assert syn_dict.find("sequence") == sorted(['järjend', 'jada', "or"])


def test_list_is_giving_dictionary():
    """Tests."""
    list_of_keys = syn_dict.list().keys()
    assert isinstance(syn_dict.list(), dict)
    assert sorted(list_of_keys) == sorted(["sequence", "järjend", "jada", "or", "loend", "nimekiri", "nimestik"])
