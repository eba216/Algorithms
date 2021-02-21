from string_algo_abc import string_algorithm_abc

class reverse(string_algorithm_abc):
    def __init__(self, string=""):
        self._string = string

    def process(self)-> str:
        return self._string[::-1]