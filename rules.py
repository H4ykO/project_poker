import random
from collections import Counter
from classes import Card, Deck

HAND_RANKINGS = {
    "Royal Flush": 10,
    "Straight Flush": 9,
    "Four of a Kind": 8,
    "Full House": 7,
    "Flush": 6,
    "Straight": 5,
    "Three of a Kind": 4,
    "Two Pairs": 3,
    "One Pair": 2,
    "High Card": 1
}

def evaluate_hands(cards):
    rank_map = {'J':11, 'Q':12, 'K': 13, 'A': 14}
    values = sorted([card.rank if isinstance(card.rank, int) else rank_map[card.rank] for card in cards])
    suits = [card.suit for card in cards]
    value_counts = Counter(values)

    is_flush = len(set(suits)) == 1
    is_straight = (values[-1] - values[0] == 4) and (len(set(values)) == 5)
    is_special_straight = set(values) == {2, 3, 4, 5, 14}

    #Royal Flush
    if is_flush and set(values) == {10, 11, 12, 13, 14}:
        return ("Royal Flush", 14)
    
    #Straight Flush
    if is_flush and (is_straight or is_special_straight):
        return("Straight Flush", 5 if is_special_straight else values[-1])
    
    #Four of a Kind
    if 4 in value_counts.values():
        quad_value = next(k for k, v in value_counts.items() if v == 4)
        return("Four of a Kind", quad_value)
    
    #Full House
    if sorted(value_counts.values()) == [2, 3]:
        trio_value = next(k for k, v in value_counts.items() if v == 3)
        pair_value = next(k for k, v in value_counts.items() if v == 2)
        return("Full House", (trio_value, pair_value))
    
    #Flush
    if is_flush:
        return("Flush", values[-1])
    
    #Straight
    if is_straight or is_special_straight:
        return("Straight", 5 if is_special_straight else values[-1])
     
    #Three of a Kind
    if 3 in value_counts.values():
        three_value = next(k for k, v in value_counts.items() if v == 3)
        return("Three of a Kind", three_value)
    
    #Two Pair
    pair_values = [k for k, v in value_counts.items() if v == 2]
    if len(pair_values) == 2:
        return ("Two Pairs", tuple(sorted(pair_values, reverse=True)))
    
    #One Pair
    if len(pair_values) == 1:
        return ("One Pair", pair_values[0])
    
    #High Card
    return("High Card", values[-1])

def get_valid_bet(prompt):
    while True:
        user_input = input(prompt).strip().lower()

        if user_input == 'check':
            return 0
        try:
            bet = int(user_input)
            if bet >= 0:
                return bet
            print("Please enter a positive number!")
        except ValueError:
            print("Please enter a valid number!")

# hand = [ 
#     Card('♥', 5),
#     Card('♣', 3),
#     Card('♥', 3),
#     Card('♠', 4),
#     Card('♥', 4),
#     ]

# result = evaluate_hands(hand)
# print(f"Hand: {result[0]} (Score: {HAND_RANKINGS[result[0]]}) Value: {result[1]}")

    