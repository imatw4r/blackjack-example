from base_deck import Deck
from blackjack_card import BlackjackCard


CARD_RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
CARD_SUITS = ["Clubs", "Hearts", "Diamonds", "Spades"]
CARD_POINTS = {
    "A": 11,
    "Q": 10,
    "J": 10,
    "K": 10,
    "10": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}


class BlackjackDeck(Deck[BlackjackCard]):
    @classmethod
    def new(cls):
        cards = [
            BlackjackCard(rank, suit) for rank in CARD_RANKS for suit in CARD_SUITS
        ]
        return cls(cards)
