from reverse_string_alg import reverse
from smallest_lexi_higher_alg import smallest_lexi_higher

algs = {"reverse": reverse,
        "smallest_lexi_higher": smallest_lexi_higher
        }


class Strings:
    def __init__(self, string, alg=None):
        self._string = string
        self._alg = alg

    def do_alg(self):

        return algs[self._alg](self._string).process()