from game import BlackjackGame
from blackjack_deck import BlackjackDeck
from blackjack_player import BlackjackPlayer, BlackjackDealer


def main():
    deck = BlackjackDeck.new()

    dealer = BlackjackDealer("Jacob", deck)
    player = BlackjackPlayer("GigaRobo")

    game = BlackjackGame(dealer=dealer, player=player)
    game.play()


if __name__ == "__main__":
    main()
