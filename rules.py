import random
from collections import Counter
from poker import Card, Deck

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
    
    #Three of a Kind
    if 3 in value_counts.values():
        three_value = [k for k, v in value_counts.items() if v == 3] [0]
        return("Three of a Kind", three_value)
    
    #Two Pair
    if list(value_counts.values()).count(2) == 2:
        pairs = sorted([k for k, v in value_counts.items() if v == 2], reverse=True)
        return("Two Pairs", pairs)
    
    #One Pair
    if 2 in value_counts.values():
        two_value = [k for k, v in value_counts.items() if v == 2] [0]
        return("One Pair", two_value)
    
    #High Card
    return("High Card", values[-1])

# hand = [ 
#     Card('♥', 'A'),
#     Card('♣', 'J'),
#     Card('♥', 5),
#     Card('♠', 4),
#     Card('♥', 3),
#     ]

# result = evaluate_hands(hand)
# print(f"Hand: {result[0]} value {result[1]}")

    