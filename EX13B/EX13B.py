"""EX13B."""


class FindPair:
    """Class for finding pairs."""

    def __init__(self, file):
        """Class constructor."""
        self.file = file
        self.dict_groups = {}
        self.big_groups = []

    def file_to_dict(self):
        """Convert information from file to the dictionary."""
        txt_file = open(self.file)
        person_group = []
        for i in txt_file:
            person_group.append(i.rstrip("\n"))

        if not person_group:
            return "This file is empty, sorry!"

        for i in person_group:
            if i.split("\t")[1] in list(self.dict_groups.keys()):
                self.dict_groups[i.split("\t")[1]].append(i.split("\t")[0])
            else:
                self.dict_groups[i.split("\t")[1]] = list([i.split("\t")[0]])
        return self.dict_groups

    def control_for_small_groups(self):
        """Control if there is only small groups in this file."""
        keys = list(self.dict_groups.keys())
        not_small_groups = []
        for i in keys:
            if len(self.dict_groups[i]) > 3:
                not_small_groups.append(self.dict_groups[i])
        return not_small_groups

    def unite_small_into_big(self):
        """Add small groups to the big ones."""
        if not self.control_for_small_groups():
            print("There is too many small groups!!!")
            raise SystemExit
        keys = list(self.dict_groups.keys())
        for i in keys:
            if len(self.dict_groups[i]) < 3:
                for j in self.dict_groups[i]:
                    self.big_groups[0].append(j)
        return self.big_groups

    def find_pair(self):
        """Find pair for every person in his group."""
        self.unite_small_into_big()
        for i in self.big_groups:
            first_name = i[0]
            for g in range(len(i) - 1):
                i[g] = i[g] + "\t" + i[g + 1]
            i[-1] = i[-1] + "\t" + first_name
        return self.big_groups

    def find_biggest_groups(self):
        """Find the biggest group or groups from all groups."""
        f_biggest_group = []
        for i in list(self.dict_groups.keys()):
            if len(self.dict_groups[i]) >= len(f_biggest_group):
                if len(self.dict_groups[i]) > len(f_biggest_group):
                    f_biggest_group = self.dict_groups[i]

        self.big_groups = []
        for i in list(self.dict_groups.keys()):
            if len(self.dict_groups[i]) == len(f_biggest_group):
                self.big_groups.append(self.dict_groups[i])
        return self.big_groups

    def print_output(self):
        """Print output."""
        for i in self.big_groups:
            for g in i:
                print(g)


a = FindPair("grupid")
a.file_to_dict()
a.find_biggest_groups()
a.control_for_small_groups()
a.unite_small_into_big()
a.find_pair()
a.print_output()
