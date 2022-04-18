import player
import deck

player1 = player.Player('one')
player2 = player.Player('two')

new_deck = deck.Deck()
new_deck.shuffle()

for i in range(26):
    player1.add_one(new_deck.deal_one())
    player2.add_one(new_deck.deal_one())

game_on = True

round_no = 0

while game_on:

    round_no += 1
    print(f'Round no: {round_no}')

    if(len(player1.all_cards) == 0):
        print(f'{player1.name} has 0 cards so {player2.name} wins')
        game_on=False
        break

    if(len(player2.all_cards) == 0):
        print(f'{player2.name} has 0 cards so {player1.name} wins')
        game_on=False
        break


    player1_cards = []
    player1_cards.append(player1.remove_one())
    
    player2_cards = []
    player2_cards.append(player2.remove_one())

    at_war = True

    while at_war:
        #get last element of array # [-1]
        if player1_cards[-1].value > player2_cards[-1].value:
            player1.add_one(player1_cards)
            player1.add_one(player2_cards)
            at_war = False
            break
        
        elif player1_cards[-1].value < player2_cards[-1].value:
            player2.add_one(player1_cards)
            player2.add_one(player2_cards)
            at_war = False
            break


        else:
            print('WAR!!!')
            
            if len(player1.all_cards) < 5:
                print(f'{player1.name} unable to declare war')
                print(f'{player2.name} wins !!')
                game_on = False
                break

            elif len(player2.all_cards) < 5:
                print(f'{player2.name} unable to declare war')
                print(f'{player1.name} wins !!')
                game_on = False
                break

            else:
                for i in range(3):
                    player1_cards.append(player1.remove_one())
                    player2_cards.append(player2.remove_one())


             

