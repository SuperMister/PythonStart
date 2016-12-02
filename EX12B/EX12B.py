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
        list_syn = []
        for i in self.synonym_list:
            if word in i.list():
                list_syn = i.list()
                list_syn.remove(word)
        return list_syn

    def list(self): # tagastab sünonüümid sõnastikuna(dict andmetüüp), kus sõna on võtmeks(key) ja selle sõna sünonüümide nimekiri(tähestiku järjekorras) on väärtuseks(value)
        synonyms = {}
        list_syn = []
        for i in self.synonym_list:
            for x in i.list():
                list_syn = i.list()
                list_syn.remove(x)
                synonyms[x] = list_syn
        return synonyms



syn1 = Synonym(['nimekiri', 'nimestik', 'loend'])
syn2 = Synonym(['järjend', 'jada', 'sequence'])
syn1.add('list')
syn2.remove('jada')
syn_dict = SynonymDictionary([syn1])
syn_dict.add(syn2)
syn_dict.find('loend')  # tagastab  ['list', 'nimekiri', 'nimestik']
syn_dict.list()  # tagastab sõnastiku:
# {
# 'list':['loend', 'nimekiri', 'nimestik'],
# 'loend':['list', 'nimekiri', 'nimestik'],
# 'nimekiri':['list', 'loend', 'nimestik'],
# 'nimestik':['list', 'loend', 'nimekiri'],
# 'järjend':['sequence'],
# 'sequence':['järjend']
# }