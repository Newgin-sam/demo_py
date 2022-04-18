import random
import constant
import card

class Deck:
    def __init__(self) -> None:

        self.all_cards = []

        for suit in constant.suit:
            for rank in constant.rank:
                new_card = card.Card(suit, rank)
                self.all_cards.append(new_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

#test

# new_deck = Deck()

# for card in new_deck.all_cards:
#     print(card)

# new_deck.shuffle()

# for card in new_deck.all_cards:
#     print(card)

# print(len(new_deck.all_cards))

# print(new_deck.deal_one())

# print(len(new_deck.all_cards))