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
    
    #Straight Flush
    if is_flush and is_straight:
        return("Straight Flush", values[-1])
    
    #Four of a Kind
    if 4 in value_counts.values():
        quad_value = [k for k, v in value_counts.items() if v == 4] [0]
        return("Four of a Kind", quad_value)
    
    #Full House
    if sorted(value_counts.values()) == [2, 3]:
        trio_value = [k for k, v in value_counts.items() if v == 3] [0]
        return("Full House", trio_value)
    
    #Flush
    if is_flush:
        return("Flush", values[-1])
    
    #Straight
    if is_straight:
        return("Straight", values[-1])
    
hand = [ 
    Card('♥', 4),
    Card('♥', 8),
    Card('♥', 6),
    Card('♥', 2),
    Card('♥', 5),
    ]

result = evaluate_hands(hand)
print(f"Hand: {result[0]} value {result[1]}")

    