"""EX11A."""


import random


class Disarrange:
    def __init__(self):
        self.initial_list = []
        self.result_list = []

    def add_value(self, value):
        self.initial_list.append(value)
        return self.initial_list

    def new_order(self):
        for i in range(len(self.initial_list) - 1):
            self.initial_list[i], self.initial_list[i + 1] = self.initial_list[i + 1], self.initial_list[i]
        self.result_list = self.initial_list
        return self.result_list

    def get_list(self, feature):
        if self.result_list is []:
            return []
        else:
            if feature == "initial":
                return self.initial_list
            if feature == "result":
                return self.result_list
