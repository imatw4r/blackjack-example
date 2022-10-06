from enum import Enum

from blackjack_player import BlackjackDealer, BlackjackPlayer, PlayerDecision


class GameDecision(str, Enum):
    PLAYER_WIN = "PLAYER_WIN"
    PLAYER_BLACKJACK = "PLAYER_BLACKJACK"
    PLAYER_LOSE = "PLAYER_LOSE"
    DEALER_WIN = "DEALER_WIN"
    DEALER_BLACKJACK = "DEALER_BLACKJACK"
    TIE = "TIE"


class BlackjackGame:
    def __init__(self, dealer: BlackjackDealer, player: BlackjackPlayer):
        self.dealer = dealer
        self.player = player

    def get_score(self, player: BlackjackPlayer):
        return sum((card.points for card in player.cards))

    def has_blackjack(self, player: BlackjackPlayer) -> bool:
        return self.get_score(player) == 21 and len(player.cards) == 2

    def display_player_hand(self) -> None:
        for card in self.player.cards:
            print(card)

    def display_dealer_hand(self, initial_round: bool = False) -> None:
        if initial_round:
            print("<REDACTED>")
            print(self.dealer.get_card(0))
        else:
            for card in self.dealer.cards:
                print(card)

    def handle_player(self, player: BlackjackPlayer, initial_round: bool = False) -> None:
        print("*" * 26)
        print("*" * 4 + f" Player {player.name} turn " + "*" * 4)
        print("*" * 26)

        self.display_player_hand()

        decision = None
        player_score = self.get_score(player)

        while player_score < 21 and decision != PlayerDecision.PASS:
            print(f"Score:", player_score)

            decision = player.decide()

            if decision == PlayerDecision.DRAW:
                player.hand_cards(self.dealer.deal_cards(1))

            player_score = self.get_score(player)

        if player_score > 21:
            print("You busted 🤪!")
            print(f"Score: {player_score}")

    def get_game_result(self, player: BlackjackPlayer) -> GameDecision:
        player_score = self.get_score(player)

        if player_score > 21:
            return GameDecision.PLAYER_LOSE

        if self.has_blackjack(self.dealer):
            if self.has_blackjack(self.player):
                return GameDecision.TIE
            else:
                return GameDecision.DEALER_BLACKJACK

        elif self.has_blackjack(self.player):
            return GameDecision.PLAYER_BLACKJACK

        elif self.get_score(self.player) < self.get_score(self.dealer):
            return GameDecision.DEALER_WIN
        elif self.get_score(self.player) > self.get_score(self.dealer):
            return GameDecision.PLAYER_WIN
        else:
            return GameDecision.TIE

    def play(self):
        self.dealer.shuffle_deck()

        self.dealer.hand_cards(self.dealer.deal_cards(number=2))
        self.player.hand_cards(self.dealer.deal_cards(number=2))

        print("*" * 26)
        print("*" * 5, " Dealer Cards ", "*" * 5)
        print("*" * 26)
        self.display_dealer_hand(initial_round=True)
        print(f"Score:", self.get_score(self.dealer))

        print()
        print("*" * 26)
        print("*" * 5, " Player Cards ", "*" * 5)
        print("*" * 26)
        self.display_player_hand()

        decision = None

        while self.get_score(self.player) < 21 and decision is not PlayerDecision.PASS:
            print(f"Score:", self.get_score(self.player))
            decision = self.player.decide()

            if decision == PlayerDecision.DRAW:
                self.player.hand_cards(self.dealer.deal_cards())

        if self.get_score(self.player) > 21:
            print("You busted 🤪!")
            print(f"Score: {self.get_score(self.player)}")
            return

        print("*" * 30)
        print("*" * 7, " Game Results ", "*" * 7)
        print("*" * 30)

        player_score = self.get_score(self.player)
        dealer_score = self.get_score(self.dealer)

        announcements = {
            GameDecision.PLAYER_WIN: f"{self.player.name} won ({player_score})!",
            GameDecision.DEALER_WIN: f"{self.dealer.name} the Dealer won with {dealer_score} points!",
            GameDecision.PLAYER_LOSE: f"{self.player.name} lose {player_score} points to {dealer_score}!",
            GameDecision.TIE: f"It's a tie! {player_score} player points to {dealer_score} dealer points.",
            GameDecision.DEALER_BLACKJACK: f"Dealer {self.dealer.name} wins by Blackjack 🎉!",
            GameDecision.PLAYER_BLACKJACK: f"{self.player.name} wins by Blackjack 🎉!",
        }

        game_result = self.get_game_result(player=self.player)

        print(announcements[game_result])
