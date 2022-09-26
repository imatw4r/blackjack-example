from functools import namedtuple


class Card:
    def __init__(self, rank: str, suite: str):
        self.rank = rank
        self.suite = suite

    def __str__(self):
        return f"{self.rank} of {self.suite}"

    def __repr__(self):
        return str(self)
