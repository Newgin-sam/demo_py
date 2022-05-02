class Chips():

    def __init__(self) -> None:
        self.total = 1000
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def loose_bet(self):
        self.total -= self.bet
