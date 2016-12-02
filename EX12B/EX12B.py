"""EX12B."""


class Synonym:
    def __init__(self, word_list):  # word_list on sünonüümide (samatähenduslike sõnade) nimekiri
        self.word_list = word_list

    def list(self):  # tagastab nimekirjana (tähestiku järjekorras) kõik sünonüümi sõnad
        return sorted(self.word_list)

    def add(self, word):  # word on sõna, mis lisatakse antud sünonüümile
        self.word_list.append(word)

    def remove(self, word):  # word on sõna, mis eemaldatakse antud sünonüümist
        if word in self.word_list:
            self.word_list.remove(word)


class SynonymDictionary:
    def __init__(self, synonym_list):  # antakse sünonüümide (Synonym isendite) nimekiri
        self.synonym_list = synonym_list
        self.word = ""
        self.list_syn = []

    def add(self, synonym):  # lisab Synonym isendi antud SynonymDictionary-sse
        if synonym not in self.synonym_list:
            self.synonym_list.append(synonym)

    def find(self, word):  # tagastab kõik antud sõna sünonüümid (mitte sõna ennast) nimekirjana (tähestiku järjekorras)
        self.word = word
        self.list_syn = []
        for i in self.synonym_list:
            if word in i.list():
                self.list_syn = i.list()
                self.list_syn.remove(word)
        return self.list_syn


    def list(self): # tagastab sünonüümid sõnastikuna(dict andmetüüp), kus sõna on võtmeks(key) ja selle sõna sünonüümide nimekiri(tähestiku järjekorras) on väärtuseks(value)
        synonyms = {}
        synonyms[self.word] = self.list_syn
        return synonyms

