from constant import value


class Hand():

    def __init__(self) -> None:
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += value[card.rank]

        if card.rank == 'Ace':
            self.aces += 1
            self.value += 11

    def adjust_for_ace(self):

        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
