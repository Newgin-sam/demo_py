
class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_one(self,new_cards):

        if(type(new_cards) == type([])):
            #for multiple
            self.all_cards.extend(new_cards)
        else:
            #for single
            self.all_cards.append(new_cards)


    def __str__(self) -> str:
        return f"Player {self.name} has {len(self.all_cards)} cards. "