import random
import chips

playing = True


def take_bet(chips):

    while True:
        try:
            chips.bet = int(input("How many chips do you want to bet"))
        except:
            print("Please! provde an integer")

        else:
            if chips.bet > chips.total:
                print(f"sorry you don't have enough chip {chips.total}")

            else:
                break


def hit(deck, hand):
    single_card = deck.deal
    hand.add_card(single_card)
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing

    while True:
        X = input("Hit or stand? Enter H / S ?")

        if X[0].upper() == 'H':
            hit(deck, hand)

        elif X[0].upper() == 'S':
            print("Player standsDealer's turn")
            Playing = False

        else:
            print("please enter H / S only")
            continue
        break


def show_some(player, dealer):

    # show only one of dealer's card
    print("\n Dealer's hand :")
    print("First card Hidden!")
    print(dealer.cards[0])

    # show all the players card
    for card in player.cards:
        print("\n player's hand :")
        print(card)


def show_all(player, dealer):

    # show all the players card
    # for card in dealer.cards:
    #     print("\n dealer's hand :")
    #     print(card)
    # does the same as the above piece of code
    print("\n Dealer's hand:", *dealer.cards, sep='\n')
    print(f"value of Dealer's hand : {dealer.value}")

    # show all the players card
    # for card in player.cards:
    #     print("\n player's hand :")
    #     print(card)
    # does the same as the above piece of code
    print("\n Player's hand:", *player.cards, sep='\n')

    print(f"value of Player's hand : {player.value}")


def player_busts(player, dealer, chips):
    print("player Busts")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("player wins !")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("dealer Busts")
    chips.lose_bet()


def dealer_wins(player, dealer, chips):
    print("dealer wins !")
    chips.win_bet()


def push(player, dealer):
    print("Dealer and Player Tie! PUSH")
