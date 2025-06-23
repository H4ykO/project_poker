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
    
class Chip:
    CHIP_VALUES = {
        'White': 1,
        'Red': 5,
        'Green': 25,
        'Black': 100,
        'Purple': 500,
        'Yellow': 1000
    }

    def __init__(self, color):
        if color not in self.CHIP_VALUES:
            raise ValueError(f"Cor de ficha inválida. Cores disponíveis: {list(self.CHIP_VALUES.keys())}")
        
        self.color = color
        self.value = self.CHIP_VALUES[color]

    def __str__(self):
        return f"{self.color} chip (${self.value})"
    
    def __repr__(self):
        return f"Chip('{self.color}')"
    
    def __eq__(self, other):
        if isinstance(other, Chip):
            return self.color == other.color
        return False

class ChipStack:
    def __init__(self, chips):
        self.chips = chips
    
    def value(self):
        return sum(chip.value for chip in self.chips)
        



