from poker import Card, Deck
from rules import evaluate_hands
from rules import HAND_RANKINGS

deck = Deck()
player_hand = deck.deal(2)
table_cards = deck.deal(5)

print("Hand: ")
for card in player_hand:
    print(f"{card.rank} of {card.suit}")

print("\nTable: ")
for i, card in enumerate(table_cards):
    if i < 3:
        print(f"Flop {i+1}: {card.rank} of {card.suit}")
    elif i == 3:
        print(f"Turn {card.rank} of {card.suit}")
    else:
        print(f"River {card.rank} of {card.suit}")

all_cards = player_hand + table_cards
result = evaluate_hands(all_cards)
print(f"\nHand: {result[0]} (Score: {HAND_RANKINGS[result[0]]}) Value: {result[1]}")