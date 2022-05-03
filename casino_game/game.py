import random
import chips
from hand import Hand
from deck import Deck
from chips import Chips
playing = True


def take_bet(chips):

    while True:
        try:
            chips.bet = int(input("How many chips do you want to bet : "))
        except:
            print("Please! provde an integer")

        else:
            if chips.bet > chips.total:
                print(f"sorry you don't have enough chip {chips.total}")

            else:
                break


def hit(deck, hand):
    single_card = deck.deal()
    print("hit")
    print(single_card)
    hand.add_card(single_card)
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing

    while True:
        X = input("Hit or stand? Enter H / S ? ")

        if X[0].upper() == 'H':
            hit(deck, hand)
        elif X[0].upper() == 'S':
            print("Player stands Dealer's turn")
            playing = False
        else:
            print("please enter H / S only")
            continue

        break

# definig type of parameter and tpe of return


def show_some(player: Hand, dealer: Hand) -> None:

    # show only one of dealer's card
    print("\n Dealer's hand :")
    print("First card Hidden!")
    print(dealer.cards[0])

    # show all the players card
    print("\n player's hand :")
    for card in player.cards:
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
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print("dealer wins !")
    chips.win_bet()


def push(player, dealer):
    print("Dealer and Player Tie! PUSH")


while True:
    print("welcome to the BlackJack")
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips = Chips()

    take_bet(player_chips)

    show_some(player_hand, dealer_hand)

    while playing:

        hit_or_stand(deck, player_hand)

        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            print("hiting")
            hit(deck, dealer_hand)

        show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif player_hand.value > dealer_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        elif player_hand.value < dealer_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand)

    print(f"\n Players total chips are at : {player_chips.total} ")

    new_game = input(" would you like to play another game? (Y / N) ")

    if new_game[0].upper() == 'Y':
        playing = True
        continue

    else:
        print("Thank you for Playing!")
        break
