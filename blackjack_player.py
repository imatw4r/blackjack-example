from typing import List
from base_player import Player
from blackjack_deck import BlackjackDeck
from blackjack_card import BlackjackCard


class BlackjackPlayer(Player):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.cards = []

    def hand_cards(self, cards: List[BlackjackCard]) -> None:
        self.cards.extend(cards)


class BlackjackDealer(BlackjackPlayer):
    def __init__(self, name: str, deck: BlackjackDeck) -> None:
        super().__init__(name)
        self.deck = deck

    def deal_cards(self, number: int = 1) -> List[BlackjackCard]:
        return self.deck.draw_card(number)

    def shuffle_deck(self):
        self.deck.shuffle()
