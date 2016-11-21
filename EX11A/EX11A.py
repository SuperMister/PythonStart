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
        for i in range(len(self.initial_list) - 1):
            self.initial_list[i], self.initial_list[i + 1] = self.initial_list[i + 1], self.initial_list[i]
        self.result_list = self.initial_list
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
