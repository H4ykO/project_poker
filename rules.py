import random
from collections import Counter
from poker import Card
from poker import Deck

def evaluate_hands(cards):
    values = sorted([card.rank if isinstance(card.rank, int) else{'J':11, 'Q':12, 'K': 13, 'A': 14}[card.rank] for card in cards])
    suits = [card.suit for card in cards]

    value_counts = Counter(values)
    is_flush = len(set(suits)) == 1
    is_straight = (values[-1] - values[0] == 4) and (len(set(values)) == 5)

    #Royal Flush
    if is_flush and set(values) == {10, 11, 12, 13, 14}:
        return ("Royal Flush", values[-1])
    
hand = [ 
    Card('♥', 'Q'),
    Card('♥', 'K'),
    Card('♥', 'A'),
    Card('♥', 10),
    Card('♥', 'J'),
    ]

# result = evaluate_hands(hand)
# print(f"Hand: {result[0]} value {result[1]}")

    