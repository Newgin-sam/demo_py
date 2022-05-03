from cgi import test
from random import random
import constant
import random
from card import Card


class Deck():
    def __init__(self) -> None:
        self.deck = []

        for suit in constant.suit:
            for rank in constant.rank:
                self.deck.append(Card(suit, rank))

    def __str__(self) -> str:
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return "The deck has :" + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


# test_deck = Deck()
# print(test_deck)
