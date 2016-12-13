"""Disarrange list."""


class Disarrange:
    """Disarrange list."""

    def __init__(self):
        """Class constructor."""
        self.initial_list = []
        self.result_list = []

    def add_value(self, value):
        """Add value to the list.

        :param value: Preferred value.
        """
        self.initial_list.append(value)
        return self.initial_list

    def new_order(self):
        """Disarrange list.

        :return: Return disarranged list.
        """
        """
        if len(self.initial_list) % 2 == 0:
            for i in range(0, 3):
                self.result_list[i].append(self.initial_list[-i-1])
                print(self.initial_list[-i-1])
                print(self.initial_list[i])
        """
        for x in self.initial_list:
            self.result_list.append(x)
        for i in range(len(self.initial_list) - 1):
            self.result_list[0] = self.initial_list[-1]
            self.result_list[i + 1] = self.initial_list[i]
        return self.result_list

    def get_list(self, feature):
        """Get chosen type of list.

        :param feature: Type of list you want to get.
        :return: Return list that has been chosen.
        """
        if self.result_list is []:
            return []
        else:
            if feature == "initial":
                return self.initial_list
            if feature == "result":
                return self.result_list

a = Disarrange()
a.add_value(1)
a.add_value(2)
a.add_value(3)
a.add_value(4)
a.add_value(5)
a.add_value(6)
print(a.get_list("initial"))
a.new_order()
print(a.get_list("result"))
print(a.get_list("initial"))
