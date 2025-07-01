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
        'Blue': 50,
        'Black': 100,
        'Purple': 500,
        'Yellow': 1000
    }
    
    def __init__(self, color):
        if color not in self.CHIP_VALUES:
            raise ValueError(f"Cor inválida. Opções: {list(self.CHIP_VALUES.keys())}")
        self.color = color
        self.value = self.CHIP_VALUES[color]
    
    def __str__(self):
        return f"{self.color} (${self.value})"
    
    def __repr__(self):
        return f"Chip('{self.color}')"
    
    def __eq__(self, other):
        if isinstance(other, Chip):
            return self.color == other.color and self.value == other.value
        return False

class ChipStack:
    def __init__(self, chips=None):
        self.chips = chips if chips else []
        self._update_total()
    
    def add_chips(self, color, quantity):
        for _ in range(quantity):
            self.chips.append(Chip(color))
        self._update_total()

    def remove_chips(self, color, quantity):
        removed = []
        chips_of_color = [chip for chip in self.chips if chip.color == color]
        
        if len(chips_of_color) < quantity:
            raise ValueError(f"Fichas insuficientes. Tentando remover {quantity}x {color}, mas só tem {len(chips_of_color)}")
        
        for chip in self.chips[:]:
            if chip.color == color and len(removed) < quantity:
                self.chips.remove(chip)
                removed.append(chip)
        
        self._update_total()
        return removed
    
    def _update_total(self):
        self.total_value = sum(chip.value for chip in self.chips)

    def get_chip_count(self):
        return Counter(chip.color for chip in self.chips)
        
    def __str__(self):
        counts = self.get_chip_count()
        return "\n".join([f"{count}x {color}" for color, count in counts.items()]) + f"\nTotal: ${self.total_value}"

class Player:
    def __init__(self, name, initial_chips):
        self.name = name
        self.stack = ChipStack()
        self.hand = []
        self.bet = 0
        
        for color, quantity in initial_chips.items():
            self.stack.add_chips(color, quantity)
    
    def place_bet(self, color, quantity):
        try:
            removed_chips = self.stack.remove_chips(color, quantity)
            self.bet += sum(chip.value for chip in removed_chips)
            return removed_chips
        except ValueError as e:
            print(f"Erro ao apostar: {e}")
            return None
        
    def show_stack(self):
        print(f"\nFichas de {self.name}:")
        print(self.stack)




        



