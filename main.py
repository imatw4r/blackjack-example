from game import BlackjackGame
from blackjack_deck import BlackjackDeck
from blackjack_player import BlackjackPlayer, BlackjackDealer


def main():
    deck = BlackjackDeck.new()

    dealer = BlackjackDealer("Jacob-Dealer", deck)
    p1 = BlackjackPlayer("Robo")
    p2 = BlackjackPlayer("Adam")

    game = BlackjackGame(dealer, players=[p1, p2])
    game.play()


if __name__ == "__main__":
    main()
