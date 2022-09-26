from base_card import Card

RANK_TO_POINTS = {
    "A": 11,
    "K": 10,
    "Q": 10,
    "J": 10,
    **{str(value): value for value in range(2, 11)},
}


class BlackjackCard(Card):
    def __init__(self, rank: str, suite: str) -> None:
        super().__init__(rank, suite)
        self.points = RANK_TO_POINTS[rank]
