from poker import Deck
from rules import evaluate_hands, HAND_RANKINGS, get_valid_bet

def main():
    deck = Deck()
    player_hand = deck.deal(2)
    table_cards = deck.deal(5)
    pot = []

    print("\nHand: ")
    for card in player_hand:
        print(f"{card.rank} of {card.suit}")

    pot.append(get_valid_bet("\nPlace your initial bet: "))
    print(f"Current pot: {sum(pot)}")

    print("\nFlop:")
    for i in range(3):
        print(f"{table_cards[i].rank} of {table_cards[i].suit}")
    
    #Flop
    pot.append(get_valid_bet("\nPlace your bet after Flop: "))
    print(f"Current pot: {sum(pot)}")

    #Turn
    print(f"\nTurn: {table_cards[3].rank} of {table_cards[3].suit}")
    pot.append(get_valid_bet("Place your bet after Turn: "))
    print(f"Current pot: {sum(pot)}")

    #River
    print(f"\nRiver: {table_cards[4].rank} of {table_cards[4].suit}")
    pot.append(get_valid_bet("Place your bet after River: "))
    print(f"Current pot: {sum(pot)}")

    all_cards = player_hand + table_cards
    result = evaluate_hands(all_cards)
    print(f"\nHand: {result[0]} (Score: {HAND_RANKINGS[result[0]]}) Value: {result[1]}")
    print(f"Total pot: {sum(pot)}")

if __name__ == "__main__":
    main()