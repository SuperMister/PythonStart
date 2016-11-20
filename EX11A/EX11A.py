"""EX11A."""


import random


class Disarrange:
    def __init__(self):
        self.initial_list = []
        self.result_list = []

    def add_value(self, value):
        return self.initial_list.append(value)

    def new_order(self):
        if len(self.initial_list) < 2:
            self.result_list = self.initial_list
            return self.result_list
        else:
            self.result_list = self.initial_list
            for i in range(0, len(self.result_list) - 1):
                random_index = random.randrange(0, len(self.result_list))
                self.result_list[i] = self.result_list[random_index]

    def get_list(self, feature):
        if self.result_list == self.initial_list:
            return []
        else:
            if feature == "initial":
                return self.initial_list
            if feature == "result":
                return self.result_list




