from typing import List, Optional
from blackjack_player import BlackjackPlayer, BlackjackDealer


class BlackjackGame:
    def __init__(self, dealer: BlackjackDealer, players: List[BlackjackPlayer]):
        self.dealer = dealer
        self.active_players = players + [dealer]
        self.inactive_players = []

    def play(self):
        self.dealer.shuffle_deck()

        for player in self.active_players:
            player.hand_cards(self.dealer.deal_cards(2))

        active_players = []
        for player in self.active_players:
            print(f"{player.name} turn.")
            print(f"Points in hand: {self.get_player_points(player)}")
            decision = input("Draw or pass? (d/p): ")

            if decision == "d":
                player.hand_cards(self.dealer.deal_cards(1))
                active_players.append(player)
            else:
                self.inactive_players.append(player)

        winners = self._select_winners(self.active_players)
        if winners is None:
            print("There is no winners yet.")
        else:
            points = self.get_player_points(winners[0])
            print("Current winners:", winners, "with number of points:", points)

        self.active_players = active_players

    def get_player_points(self, player: BlackjackPlayer) -> int:
        return sum((c.points for c in player.cards))

    def is_loser(self, player: BlackjackPlayer) -> bool:
        return self.get_player_points(player) > 21

    def _select_winners(
        self, players: List[BlackjackPlayer]
    ) -> Optional[List[BlackjackPlayer]]:
        winners = []
        max_points = 0
        for player in players:
            if self.is_loser(player):
                continue

            player_points = self.get_player_points(player)

            if max_points == player_points:
                winners.append(player)
            elif max_points < player_points:
                max_points = player_points
                winners = [player]
        return winners
