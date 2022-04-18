import constant

class Card:
    def __init__(self,suit,rank) -> None:
        self.suit = suit
        self.rank = rank
        self.value = constant.value[rank]
        

    def __str__(self) -> str:
        return self.rank +' of '+ self.suit

#test

# queen_of_hearts = Card('Heart','Queen')
# print(queen_of_hearts)
# print(queen_of_hearts.value)