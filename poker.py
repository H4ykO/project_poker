import random
from collections import Counter

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} {self.suit}"
    
class Deck:
    def __init__(self):
        suits = ['♦', '♠', '♥', '♣']
        ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]
        random.shuffle(self.cards)

    def deal(self, num_cards):
        return [self.cards.pop() for _ in range(num_cards)]
    
# deck = Deck()
# player_hand = deck.deal(2)
# flop = deck.deal(3)
# turn = deck.deal(1)
# river = deck.deal(1)


