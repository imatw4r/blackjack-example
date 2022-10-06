from dataclasses import is_dataclass
from enum import Enum
from typing import List, Optional

from blackjack_player import BlackjackDealer, BlackjackPlayer, PlayerDecision


class GameDecision(str, Enum):
    WIN = "WIN"
    LOSE = "LOSE"
    TIE = "TIE"


class BlackjackGame:
    def __init__(self, dealer: BlackjackDealer, players: List[BlackjackPlayer]):
        self.dealer = dealer
        self.players = players

    def display_hand(self, player: BlackjackPlayer, initial_round: bool = False):
        if player.is_dealer() and initial_round:
            print("<REDACTED>")
            print(player.get_card(0))
        else:
            for card in player.cards:
                print(card)

    def handle_player(self, player: BlackjackPlayer, initial_round: bool = False) -> None:
        print("*" * 26)
        print("*" * 4 + f" Player {player.name} turn " + "*" * 4)
        print("*" * 26)

        self.display_hand(player=player, initial_round=initial_round)

        decision = None

        while player.score() < 21 and decision != PlayerDecision.PASS:
            print(f"Score:", player.score())

            decision = player.decide()

            if decision == PlayerDecision.PASS:
                return

            player.hand_cards(self.dealer.deal_cards(1))

        if player.score() > 21:
            print("You busted 🤪!")
            print(f"Score: {player.score()}")

    def get_game_result(self, player: BlackjackPlayer) -> GameDecision:
        player_score = player.score()

        if player_score > 21:
            return GameDecision.LOSE

        elif player.has_blackjack() and self.dealer.has_blackjack():
            return GameDecision.TIE

        elif player.has_blackjack() and not self.dealer.has_blackjack():
            return GameDecision.WIN

        if player_score > self.dealer.score():
            return GameDecision.WIN

        elif player_score < self.dealer.score():
            return GameDecision.LOSE
        else:
            return GameDecision.TIE

    def play(self):
        self.dealer.shuffle_deck()

        self.dealer.hand_cards(self.dealer.deal_cards(2))

        for player in self.players:
            player.hand_cards(self.dealer.deal_cards(number=2))

        print("*" * 26)
        print("*" * 5, " Dealer Cards ", "*" * 5)
        print("*" * 26)
        self.display_hand(player=self.dealer, initial_round=True)

        for player in self.players:
            self.handle_player(player)

        game_results = [(player, self.get_game_result(player)) for player in self.players]
        dealer_wins = len([result for _, result in game_results if result == GameDecision.WIN]) == 0

        print("*" * 30)
        print("*" * 7, " Game Results ", "*" * 7)
        print("*" * 30)

        if dealer_wins:
            print(f"{self.dealer.name} dealer wins with points {self.dealer.score()}")
            return

        for player, result in game_results:
            if result == GameDecision.LOSE:
                print(f"Player {player.name} lost.")
            elif result == GameDecision.WIN:
                print(f"Player {player.name} won.")
            elif result == GameDecision.TIE:
                print(f"Player {player.name} tied.")
