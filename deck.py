import random


class Card:

    def __init__(self, suit, value, face):
        self.suit = suit
        self.value = value
        self.face = face

    def __repr__(self):
        return '({},{})'.format(self.suit, self.value)

    def __gt__(self, other):
        if self.value.isalpha() and other.value.isdigit():
            return True
        if other.value.isalpha() and self.value.isdigit():
            return False

        if self.value.isalpha() and other.value.isalpha():
            if self.value == 'A' and other.value != 'A':
                return True
            elif self.value == 'K' and (other.value == 'Q' or other.value == 'J'):
                return True
            elif self.value == 'Q' and other.value == 'J':
                return True
            else:
                return False
        if self.value.isdigit() and other.value.isdigit():
            return (int(self.value) > int(other.value))

    def __eq__(self, other):
        if self.value == other.value:
            return True

        return False


class Deck:

    card_decks = []

    def __init__(self):
        suits = ['H', 'S', 'C', 'D']
        values = ['A', 'K', 'Q', 'J', '10', '9',
                  '8', '7', '6', '5', '4', '3', '2']
        # card_decks = [card for suit in suits for value in values card = Card(suit, value)]
        for suit in suits:
            for value in values:
                card = Card(suit, value, False)
                self.card_decks.append(card)

        random.shuffle(self.card_decks)

    def get_deck(self):
        return (self.card_decks)
