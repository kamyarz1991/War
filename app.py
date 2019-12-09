from deck import Deck
from deck import Card
from game import Play

# It is a slightly different variation of the 'WAR' card game. Users can select which card to throw unless
# they are in a WAR situation, which all the cards will be from the top.

if __name__ == "__main__":

    deck = Deck()
    player_pc = []
    player_real = []
    for i in range(len(deck.get_deck())):
        if i % 2 == 0:
            player_pc.append(deck.get_deck()[i])
        else:
            player_real.append(deck.get_deck()[i])

    game = Play(player_pc, player_real)
    # game = Play([Card('S', '2', False), Card('D', '2', False), Card('H', '2', False), Card('C', '2', False)],
    #            [Card('S', 'A', False), Card('D', 'A', False), Card('H', 'A', False), Card('C', 'A', False)])
    game.play()
