from enum import Enum
from typing import List, Literal

from base_player import Player
from blackjack_card import BlackjackCard
from blackjack_deck import BlackjackDeck


class PlayerDecision(str, Enum):
    PASS = "PASS"
    DRAW = "DRAWW"


class BlackjackPlayer(Player):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.cards: List[BlackjackCard] = []

    def hand_cards(self, cards: List[BlackjackCard]) -> None:
        self.cards.extend(cards)

    def is_dealer(self) -> bool:
        return False

    def get_card(self, idx: int) -> BlackjackCard:
        return self.cards[idx]

    def decide(self) -> PlayerDecision:
        """
        Handle player decision.
        """
        decision = input("What to do? (d)raw or (p)ass? ").upper()
        while decision not in ["D", "P"]:
            print("Invalid input. Must be one of 'd' or 'p'.")
            decision = input("What to do? (d)raw or (p)ass? ").upper()

        return PlayerDecision.DRAW if decision == "D" else PlayerDecision.PASS


class BlackjackDealer(BlackjackPlayer):
    def __init__(self, name: str, deck: BlackjackDeck) -> None:
        super().__init__(name)
        self.deck = deck

    def deal_cards(self, number: int = 1) -> List[BlackjackCard]:
        return self.deck.draw_card(number)

    def shuffle_deck(self) -> None:
        self.deck.shuffle()

    def is_dealer(self) -> bool:
        return True

    def decide(self) -> PlayerDecision:
        """
        Handle dealer decision.
        """
        return PlayerDecision.DRAW if self.score() < 16 else PlayerDecision.PASS
