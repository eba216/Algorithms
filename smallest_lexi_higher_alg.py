# smallest lexicographically higher string possible

from string_algo_abc import string_algorithm_abc

class smallest_lexi_higher(string_algorithm_abc):
    def __init__(self, string=""):
        self._string = string

    def process(self)-> str:
        new_word = ""

        index = len(self._string) - 1
        while index > 0 and self._string[index - 1] >= self._string[index]:
            index -= 1

        if index <= 0:
            return "no answer"

        j = len(self._string) - 1
        while self._string[j] <= self._string[index - 1]:
            j -= 1

        new_word += self._string[:index - 1]
        new_word += self._string[j]

        i = len(self._string) - 1
        while i > index - 1:
            if i == j:
                new_word += self._string[index - 1]
                i -= 1
            else:
                new_word += self._string[i]
                i -= 1

        return new_word
