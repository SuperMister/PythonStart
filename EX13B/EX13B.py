"""EX13B."""


import random


class FindPair:
    """Class for finding pairs"""

    def __init__(self, file):
        self.file = file
        self.dict_groups = {}
        self.biggest_group = []
        self.all_pairs = []

    def file_to_dict(self):
        """Convert information from file to the dictionary."""
        y = open(self.file)
        person_group = []
        for i in y:
            person_group.append(i.rstrip("\n"))
        for i in person_group:
            if i.split("\t")[1] in list(self.dict_groups.keys()):
                self.dict_groups[i.split("\t")[1]].append(i.split("\t")[0])
            else:
                self.dict_groups[i.split("\t")[1]] = list([i.split("\t")[0]])
        return self.dict_groups

    def find_pair(self):
        """Find pair for every person in all groups."""
        keys = list(self.dict_groups.keys())
        group_remove = []
        while True:
            for y in keys:
                if len(self.dict_groups[y]) < 3:
                    for i in self.dict_groups[y]:
                        b = random.choice(self.biggest_group)
                        self.all_pairs.append(i + "\t " + b)
                else:
                    for j in self.dict_groups[y]:
                        e = random.choice(self.dict_groups[y])
                        if j != e:
                            self.all_pairs.append(j + "\t" + e)
                        else:
                            for g in self.dict_groups[y]:
                                group_remove.append(g)
                            group_remove.remove(j)
                            e = random.choice(group_remove)
                            self.all_pairs.append(j + "\t" + e)
            return self.all_pairs

    def find_biggest_group(self):
        """Find the biggest group from all groups."""
        self.biggest_group = []
        for i in list(self.dict_groups.keys()):
            if len(self.dict_groups[i]) > len(self.biggest_group):
                self.biggest_group = self.dict_groups[i]

        return self.biggest_group

    def print_output(self):
        for i in self.all_pairs:
            print(i)


a = FindPair("grupid.txt")
a.file_to_dict()
a.find_biggest_group()
a.find_pair()
a.print_output()
