import random
from typing import List
from typing import TypeVar, Generic

T_card = TypeVar("T_card")


class Deck(Generic[T_card]):
    def __init__(self, cards: List[T_card]) -> None:
        self.cards = cards

    def draw_card(self, number: int) -> List[T_card]:
        return [self.cards.pop() for _ in range(number)]

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def __str__(self) -> str:
        return f"{self.__class__.__qualname__} with {len(self.cards)} cards."
