"""Dictionary of synonyms."""


class Synonym:
    """Class of synonyms."""

    def __init__(self, word_list):
        """Class constructor."""
        self.word_list = word_list

    def list(self):
        """Return sorted list of words."""
        return sorted(self.word_list)

    def add(self, word):
        """Add word to the list of words."""
        self.word_list.append(word)

    def remove(self, word):
        """Remove word from the list of words."""
        if word in self.word_list:
            self.word_list.remove(word)


class SynonymDictionary:
    """Class of SynonymDictionary."""

    def __init__(self, synonym_list):
        """Class constructor."""
        self.synonym_list = synonym_list

    def add(self, synonym):
        """Add synonym to the list of synonyms."""
        if synonym not in self.synonym_list:
            self.synonym_list.append(synonym)

    def find(self, word):
        """Find synonyms for the given word."""
        list_syn = []
        for i in self.synonym_list:
            if word in i.list():
                list_syn = i.list()
                list_syn.remove(word)
        return list_syn

    def list(self):
        """Create dictionary with synonyms for every word."""
        synonyms = {}
        list_syn = []
        for i in self.synonym_list:
            for x in i.list():
                list_syn = i.list()
                list_syn.remove(x)
                synonyms[x] = list_syn
        return synonyms
