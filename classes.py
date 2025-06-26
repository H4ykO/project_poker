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
    
    def add_chips(self, color, quantity):
        for _ in range(quantity):
            self.chips.append(Chip(color))
        self._update_total()

    def remove_chips(self, color, quantity):
        removed = []
        remaining = quantity
    
        chips_of_color = [chip for chip in self.chips if chip.color == color]

        if len(chips_of_color) < quantity:
            raise ValueError(f"insuficient chips, trying to remove {quantity}x {color}, but only has {len{chips_of_color}}")
        
        for chip in self.chips[:]:
            if chip.color == color and remaining > 0:
                self.chips.remove(chip)
                removed.append(chip)
                remaining -= 1
        
        self._update_total()
        return removed
    
    def _update_total(self):
        self.total_value = sum(chip.value for chip in self.chips)

    def get_chip_count(self):
        count = []
        for chip in self.chips:
            count[chip.color] = count.get(chip.color, 0) + 1
            return count
        
    def __str__(self):
        counts = self.get_chip_count()
        return "\n" .join([f"{count}x {color}" for color, count in counts.items()]) +f"\nTotal: ${self.total_value}"
        



