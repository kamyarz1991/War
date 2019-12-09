from random import randint
from deck import Card
import random


class Play:

    pc_facedup = 0
    user_facedup = 0

    def __init__(self, pc_deck, user_deck):
        self.pc_deck = pc_deck
        self.user_deck = user_deck

    def play(self):
        print(self.user_deck)
        while (len(self.pc_deck) != 0 and len(self.user_deck) != 0):
            while True:
                try:
                    user_card_index = int(input(
                        'please enter a number from {} to {}: '.format(self.user_facedup, len(self.user_deck)-1)))
                    if user_card_index < self.user_facedup or user_card_index >= len(self.user_deck):
                        raise ValueError
                except ValueError as v:
                    print("Wrong input try again")
                    continue
                else:
                    user_card = self.user_deck.pop(user_card_index)
                    user_card.face = True
                    break

            pc_card_index = randint(self.pc_facedup, len(self.pc_deck)-1)
            pc_card = self.pc_deck.pop(pc_card_index)
            pc_card.face = True

            if pc_card > user_card:
                self.pc_deck.insert(0, user_card)
                self.pc_deck.insert(0, pc_card)
                self.pc_facedup += 2
                print('PC card {} beats YOUR card {}'.format(pc_card, user_card))

            elif user_card > pc_card:
                self.user_deck.insert(0, user_card)
                self.user_deck.insert(0, pc_card)
                self.user_facedup += 2
                print('YOUR card {} beats PC card {}'.format(user_card, pc_card))

            else:
                self.war(user_card, pc_card)

            if self.user_facedup == len(self.user_deck):
                self.reshuffle_deck(self.user_deck)
                self.user_facedup = 0

            if self.pc_facedup == len(self.pc_deck):
                self.reshuffle_deck(self.pc_deck)
                self.pc_facedup = 0
        winner = "PC Wins" if len(self.user_deck) == 0 else "YOU win"
        print(winner)

    def war(self, user_card, pc_card):
        pc_buffer = []
        user_buffer = []

        pc_buffer.append(pc_card)
        user_buffer.append(user_card)
        ptr1 = 1
        ptr2 = 5
        while pc_card == user_card:
            print("We are in war now")
            print('Both PC card {} and YOUR card {} have the same values'.format(
                pc_card, user_card))
            for _ in range(ptr1, ptr2):
                try:
                    if len(self.pc_deck) == 0:
                        winner = "PC ran out of card YOU win"
                        raise Exception
                    if len(self.user_deck) == 0:
                        winner = "YOU ran out of card PC wins"
                        raise Exception
                except Exception as e:
                    print(winner)
                    exit()
                else:
                    if self.pc_deck[len(self.pc_deck) - 1].face == True:
                        self.reshuffle_deck(self.pc_deck)
                        self.pc_facedup = 0
                    if self.user_deck[len(self.user_deck) - 1].face == True:
                        self.reshuffle_deck(self.user_deck)
                        self.user_facedup = 0

                pc_buffer.append(self.pc_deck.pop(len(self.pc_deck) - 1))
                user_buffer.append(self.user_deck.pop(len(self.user_deck) - 1))

            pc_card = pc_buffer[len(pc_buffer)-1]
            user_card = user_buffer[len(user_buffer)-1]
            ptr1 = 0
            ptr2 = 2

        if pc_card > user_card:
            print('PC card {} beats YOUR card {}'.format(pc_card, user_card))
            for c in pc_buffer:
                self.pc_deck.insert(0, c)
            for u in user_buffer:
                self.pc_deck.insert(0, u)
            self.pc_facedup += len(pc_buffer) + len(user_buffer)

        if user_card > pc_card:
            print('YOUR card {} beats PC card {}'.format(user_card, pc_card))
            for c in pc_buffer:
                self.user_deck.insert(0, c)
            for u in user_buffer:
                self.user_deck.insert(0, u)
            self.user_facedup += len(pc_buffer) + len(user_buffer)

    def reshuffle_deck(self, deck):
        for card in deck:
            card.face = False
        random.shuffle(deck)
